import json
from aiohttp import web
# local
from core import query_string_parser as qsp
import get_homologous_genes.business as business


async def handler(app, raw_params):
  # parse the parameters
  params = qsp.validate(
    raw_params,
    {
      'chromosome': qsp.Parser(qsp.Type.NON_EMPTY_STRING),
      'families': qsp.Parser(qsp.Type.STRING_LIST),
    }
  )
  # process the request
  return await business.globalPlot(
    app['r_engine'],
    app['rpc'],
    params['chromosome'],
    params['families']
  )


method = 'GET'
path = '/macro/get-homologous-genes'#?chromosome&families  # global plots
async def webHandler(request):
  try:
    params = request.query
    response = await handler(request.app, params)
    return web.Response(text=json.dumps(response), status=200)
  except Exception as e:
    response_obj = {'status' : 'failed', 'reason': str(e)}
    return web.Response(text=json.dumps(response_obj), status=500)


route = method, path, handler, webHandler