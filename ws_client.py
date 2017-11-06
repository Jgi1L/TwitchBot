import asyncio
import aiohttp
import async_timeout
from irc3 import plugin
import irc3
from throttle_bag import Throttle



@plugin
class WebClient(object):
    def __init__(self, bot):
        self.bot = bot
        self.channel = bot.config.channel

    @irc3.event(irc3.rfc.CONNECTED)
    def connected(self, **kw):
        self.bot.join(self.bot.config.channel)
        asyncio.Task(self.ws_client())

    
    @irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        """Say hi when someone join a channel"""
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, 'Hi %s!' % mask.nick)
        else:
            self.bot.privmsg(channel, 'Hi!')
   

    async def ws_client(self):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('http://127.0.0.1:8080') as ws:
                async for msg in ws:
                    print(msg)
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        message = msg.data.split(':')
                        if message[0] == 'close cmd':
                            await ws.close()
                            break
                        if message[0] == 'fuck you':
                            self.bot.privmsg(self.channel, "Fuck you")
                        if message[0] == 'spam':
                            await self.spam_message(int(message[2]), message[1], self.channel)
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        break
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        break

    async def spam_message(self, spam_num, message, target):
        double_message = message + " " + message
        for i in range(0,spam_num + 1):
            if i%2:
                self.bot.privmsg(target, message)
            if i%3:
                self.bot.privmsg(target, double_message)
            
            await asyncio.sleep(1.5)
