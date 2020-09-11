# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chromosomesearch_pb2 as chromosomesearch__pb2


class ChromosomeSearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/chromosomesearch.ChromosomeSearch/Search',
                request_serializer=chromosomesearch__pb2.SearchRequest.SerializeToString,
                response_deserializer=chromosomesearch__pb2.SearchReply.FromString,
                )


class ChromosomeSearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChromosomeSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=chromosomesearch__pb2.SearchRequest.FromString,
                    response_serializer=chromosomesearch__pb2.SearchReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chromosomesearch.ChromosomeSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChromosomeSearch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chromosomesearch.ChromosomeSearch/Search',
            chromosomesearch__pb2.SearchRequest.SerializeToString,
            chromosomesearch__pb2.SearchReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
