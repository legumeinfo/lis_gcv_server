# dependencies
import grpc
from grpc.experimental import aio
# module
from pairwise_macro_synteny_blocks.proto.pairwisemacrosyntenyblocks_service.v1 import pairwisemacrosyntenyblocks_pb2
from pairwise_macro_synteny_blocks.proto.pairwisemacrosyntenyblocks_service.v1 import pairwisemacrosyntenyblocks_pb2_grpc
from pairwise_macro_synteny_blocks.proto.block.v1 import block_pb2


class PairwiseMacroSyntenyBlocks(pairwisemacrosyntenyblocks_pb2_grpc.PairwiseMacroSyntenyBlocksServicer):

  def __init__(self, handler):
    self.handler = handler

  async def Compute(self, request, context):
    chromosome = request.chromosome
    target = request.target
    matched = request.matched
    intermediate = request.intermediate
    mask = request.mask
    metrics = request.optionalMetrics
    min_chromosome_genes = request.optionalChromosomeGenes
    try:
      self.handler.parseArguments(chromosome, target, matched, intermediate, mask, metrics, min_chromosome_genes)
    except:
      # raise a gRPC INVALID ARGUMENT error
      await context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'Required arguments are missing or given arguments have invalid values')
    blocks = await self.handler.process(chromosome, target, matched, intermediate, mask, metrics, min_chromosome_genes)
    if blocks is None:
      # raise a gRPC NOT FOUND error
      await context.abort(grpc.StatusCode.NOT_FOUND, 'Chromosome not found')
    block_messages = list(map(lambda b:
      block_pb2.Block(
          i=b['i'],
          j=b['j'],
          fmin=b['fmin'],
          fmax=b['fmax'],
          orientation=b['orientation'],
          optionalMetrics=b.get('optionalMetrics', [])
      ), blocks))
    return pairwisemacrosyntenyblocks_pb2.PairwiseMacroSyntenyBlocksComputeReply(blocks=block_messages)


async def run_grpc_server(host, port, handler):
  server = aio.server()
  server.add_insecure_port(f'{host}:{port}')
  servicer = PairwiseMacroSyntenyBlocks(handler)
  pairwisemacrosyntenyblocks_pb2_grpc\
    .add_PairwiseMacroSyntenyBlocksServicer_to_server(servicer, server)
  await server.start()
  await server.wait_for_termination()
