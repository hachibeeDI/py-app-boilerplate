import re
import json
import sys
from glob import glob
from importlib import import_module
from types import FunctionType
from logging import basicConfig, getLogger, DEBUG

import tornado.ioloop
import tornado.web

from json_rpc import register, rpc_dispatcher, make_request
from json_rpc.server.http import create_handler


basicConfig(level=DEBUG)
logger = getLogger(__name__)


def auto_register_rpc_modules():
    # TODO: concurrent
    for orig_path in glob('rpc/**/*.py'):
        path_for_importlib = orig_path[:-3].replace('/', '.')
        module = import_module(path_for_importlib)
        available_functions = filter(
            lambda m: isinstance(m, FunctionType),
            (getattr(module, attr) for attr in dir(module) if not attr.startswith('_')))

        prefix = path_for_importlib.replace('rpc.', '')
        for fu in available_functions:
            rpc_name = f'{prefix}.{fu.__name__}' 
            logger.debug(f'register RPC {rpc_name}')
            register(rpc_name)(fu)


if __name__ == '__main__':
    auto_register_rpc_modules()

    ARGV = dict(enumerate(sys.argv))

    def make_app():
        return tornado.web.Application([
            (r'/rpc', create_handler(tornado.web.RequestHandler)),
        ])

    app = make_app()
    port = ARGV.get(1, 8888)
    app.listen(port)
    logger.debug(f'starting server with {port}')
    tornado.ioloop.IOLoop.current().start()
