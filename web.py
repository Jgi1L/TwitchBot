import asyncio
import aiohttp
import async_timeout
from irc3 import plugin



@plugin
class WebClient(object):
    def __init__(self, bot):
        self.bot = bot
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.ws_client())


    async def ws_client(self):
        session = aiohttp.ClientSession()

        async with sesssion.ws_connect('http://127.0.0.1:8080') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == 'close cmd':
                        await ws.close()
                        break
                    else:
                        await ws.send_str(msg.data + '/answer')
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

