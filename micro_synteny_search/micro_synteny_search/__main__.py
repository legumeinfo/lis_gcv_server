#!/usr/bin/env python

# Python
import argparse
import asyncio
import logging
import os
import uvloop
# module
import micro_synteny_search
from micro_synteny_search.database import connectToRedis
from micro_synteny_search.grpc_server import run_grpc_server
from micro_synteny_search.http_server import run_http_server
from micro_synteny_search.request_handler import RequestHandler


LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
  }


# a class that loads argument values from command line variables, resulting in a
# value priority: command line > environment variable > default value
class EnvArg(argparse.Action):

  def __init__(self, envvar, required=False, default=None, **kwargs):
    if envvar in os.environ:
      default = os.environ[envvar]
    if required and default is not None:
      required = False
    super(EnvArg, self).__init__(default=default, required=required, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
    setattr(namespace, self.dest, values)



def parseArgs():

  # create the parser
  parser = argparse.ArgumentParser(
    prog=micro_synteny_search.__version__,
    description='A microservice for finding chromosome names similar to the given query.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
    '--version',
    action='version',
    version=f'%(prog)s {micro_synteny_search.__version__} schema {micro_synteny_search.__schema_version__}',
  )

  # logging args
  loglevel_envvar = 'LOG_LEVEL'
  parser.add_argument(
    '--log-level',
    dest='log_level',
    action=EnvArg,
    envvar=loglevel_envvar,
    type=str,
    choices=list(LOG_LEVELS.keys()),
    default='WARNING',
    help=('What level of events should be logged (can also be specified using '
          f'the {loglevel_envvar} environment variable).'))
  logfile_envvar = 'LOG_FILE'
  parser.add_argument(
    '--log-file',
    dest='log_file',
    action=EnvArg,
    default=argparse.SUPPRESS,  # removes "(default: None)" from help text
    envvar=logfile_envvar,
    type=str,
    help=('The file events should be logged in (can also be specified using '
          f'the {logfile_envvar} environment variable).'))

  # Async HTTP args
  parser.add_argument('--no-http', dest='nohttp', action='store_true', help='Don\'t run the HTTP server.')
  parser.set_defaults(nohttp=False)
  hhost_envvar = 'HTTP_HOST'
  parser.add_argument('--hhost', action=EnvArg, envvar=hhost_envvar, type=str, default='localhost', help=f'The HTTP server host (can also be specified using the {hhost_envvar} environment variable).')
  hport_envvar = 'HTTP_PORT'
  parser.add_argument('--hport', action=EnvArg, envvar=hport_envvar, type=str, default='8080', help=f'The HTTP server port (can also be specified using the {hport_envvar} environment variable).')

  # gRPC args
  parser.add_argument('--no-grpc', dest='nogrpc', action='store_true', help='Don\'t run the gRPC server.')
  parser.set_defaults(nogrpc=False)
  ghost_envvar = 'GRPC_HOST'
  parser.add_argument('--ghost', action=EnvArg, envvar=ghost_envvar, type=str, default='[::]', help=f'The gRPC server host (can also be specified using the {ghost_envvar} environment variable).')
  gport_envvar = 'GRPC_PORT'
  parser.add_argument('--gport', action=EnvArg, envvar=gport_envvar, type=str, default='8081', help=f'The gRPC server port (can also be specified using the {gport_envvar} environment variable).')

  # Redis args
  rdb_envvar = 'REDIS_DB'
  parser.add_argument('--rdb', action=EnvArg, envvar=rdb_envvar, type=int, default=0, help=f'The Redis database (can also be specified using the {rdb_envvar} environment variable).')
  rpassword_envvar = 'REDIS_PASSWORD'
  parser.add_argument('--rpassword', action=EnvArg, envvar=rpassword_envvar, type=str, help=f'The Redis password (can also be specified using the {rpassword_envvar} environment variable).')
  rhost_envvar = 'REDIS_HOST'
  parser.add_argument('--rhost', action=EnvArg, envvar=rhost_envvar, type=str, default='localhost', help=f'The Redis host (can also be specified using the {rhost_envvar} environment variable).')
  rport_envvar = 'REDIS_PORT'
  parser.add_argument('--rport', action=EnvArg, envvar=rport_envvar, type=int, default=6379, help=f'The Redis port (can also be specified using the {rport_envvar} environment variable).')

  return parser.parse_args()


# the main coroutine that starts the various program tasks
async def main_coroutine(args):
  redis_connection = await connectToRedis(args.rhost, args.rport, args.rdb, args.rpassword)
  handler = RequestHandler(redis_connection)
  tasks = []
  if not args.nohttp:
    http_task = asyncio.create_task(run_http_server(args.hhost, args.hport, handler))
    tasks.append(http_task)
  if not args.nogrpc:
    grpc_task = asyncio.create_task(run_grpc_server(args.ghost, args.gport, handler))
    tasks.append(grpc_task)
  await asyncio.gather(*tasks)


def main():

  # parse the command line arguments / environment variables
  args = parseArgs()
  if args.nohttp and args.nogrpc:
    exit('--no-http and --no-grpc can\'t both be given')

  # setup logging
  log_config = {
      'level': LOG_LEVELS[args.log_level],
    }
  if 'log_file' in args:
    log_config['filename'] = args.log_file
  logging.basicConfig(**log_config)

  # initialize asyncio
  loop = uvloop.new_event_loop()
  asyncio.set_event_loop(loop)

  # run the program
  loop.create_task(main_coroutine(args))
  loop.run_forever()


if __name__ == '__main__':
  main()
