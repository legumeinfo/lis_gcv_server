# dependencies
import aiohttp_cors
from aiohttp import web


async def http_post_handler(request):
  # parse the chromosome and parameters from the POST data
  data = await request.json()
  chromosome = data.get('chromosome')
  target = data.get('target')
  matched = data.get('matched')
  intermediate = data.get('intermediate')
  mask = data.get('mask')
  metrics = data.get('optionalMetrics')
  min_chromosome_genes = data.get('optionalChromosomeGenes', matched)
  min_chromosome_length = data.get('optionalChromosomeLength', matched)
  handler = request.app['handler']
  try:
    chromosome, target, matched, intermediate, mask, metrics, min_chromosome_genes, min_chromosome_length = \
      handler.parseArguments(chromosome, target, matched, intermediate, mask, metrics, min_chromosome_length)
  except:
    return web.HTTPBadRequest(text='Required arguments are missing or have invalid values')
  blocks = await handler.process(chromosome, target, matched, intermediate, mask, metrics, min_chromosome_genes, min_chromosome_length)
  if blocks is None:
    return web.HTTPNotFound(text='Chromosome not found')
  return web.json_response({'blocks': blocks})


async def run_http_server(host, port, handler):
  # make the app
  app = web.Application()
  app['handler'] = handler
  # define the route and enable CORS
  cors = aiohttp_cors.setup(app, defaults={
    '*': aiohttp_cors.ResourceOptions(
           allow_credentials=True,
           expose_headers='*',
           allow_headers='*',
         )
  })
  route = app.router.add_post('/', http_post_handler)
  cors.add(route)
  # run the app
  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, host, port)
  await site.start()
