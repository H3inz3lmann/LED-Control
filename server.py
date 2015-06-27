__author__ = 'matthias'

import asyncio
from aiohttp import web

class Server():
    def __init__(self):
        self.app = web.Application(loop=loop)
        self.app.router.add_route('GET', '/{name}', handle)

    def 



loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass