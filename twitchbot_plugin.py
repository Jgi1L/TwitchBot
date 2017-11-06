from irc3.plugins.command import command
import asyncio
#from aiohttp import wsgi
#from aiohttp import web
from throttle_bag import Throttle
import irc3
import logging
import json


@irc3.plugin
class Plugin(object):
    

    def __init__(self, bot):
        self.bot = bot
        self.message_count = 1 
        self.throttler = Throttle(bot, seconds=30, times=20, aio=True)

    @irc3.event(irc3.rfc.CONNECTED)
    def connected(self, **kw):
        self.bot.join(self.bot.config.channel)

    @irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        """Say hi when someone join a channel"""
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, 'Hi %s!' % mask.nick)
        else:
            self.bot.privmsg(channel, 'Hi!')
    
    """
    @irc3.event(irc3.rfc.PRIVMSG)
    async def on_privmsg(self, data, event, mask, target):
       # Only spam if the message is sent by a none bot 
        for i in range(0,3):
            data = data + " " + data
            self.bot.privmsg(target, data)
            await asyncio.sleep(1.2)
        
    """

    async def spam_message(self, spam_num, message, target):
        double_message = message + " " + message
        for i in range(0,spam_num + 1):
            if i%2:
                self.throttler.privmsg(target, message)
            if i%3:
                self.throttler.privmsg(target, double_message)
            
            await asyncio.sleep(1.5)


    @command(permission='view')
    async def spam(self, mask, target, args):
        """Spam Message

            %%spam <message>...
        """
        spam_num = int(args['<message>'][0])
        message = ' '.join(args['<message>'][1:len(args['<message>'])])
        await self.spam_message(spam_num, message, target)


def main():
    loop = asyncio.get_event_loop()
    #loop.set_debug(True)
    config = {
        'loop': loop,
        'nick': 'jaygi1l',
        'password': 'oauth:hh3ytxvrnt46cbc78dkd70wksnkrr6',
        #'channel': '#greekgodx',
        'channel': '#jgi1l',
        'host': 'irc.twitch.tv',
        'port': '6667',
        #'debug': True,
        'verbose': True,
        'raw': True,
        'irc3.plugins.logger': {
            'handler' : 'irc3.plugins.logger.file_handler',
            'filename': 'C:\Code\TwitchSpamBot\TwitchBot\log.txt',
        },
        'irc3.plugins.command': {
            'cmd' : '&&',
        },
        'includes': [
            #'twitchbot_plugin', 
            'ws_client',
            'irc3.plugins.command', 
            #'irc3.plugins.log', 
            'irc3.plugins.logger',
            #'mycommands',
        ],
    }      

    bot = irc3.IrcBot.from_config(config)
    bot.run(forever=False)
    #bot = createBot(config)
    #bot.privmsg(bot.config.channel, 'Fuck you')

    config.update({
        'nick': 'pls_fk_me_daddy',
        'password': 'oauth:x6ggybxb3duyrmq9stahukkm0kicua',
    })
    bot2 = irc3.IrcBot.from_config(config)
    bot2.run(forever=False)

    config.update({
        'nick': 'reformed_nogg',
        'password': 'oauth:8uwvgrwxkj5302yyj1uql6ykmpy79w',
    })
    bot3 = irc3.IrcBot.from_config(config)
    bot3.run(forever=False)

    config.update({
        'nick': 'poor_people_are_gross',
        'password': 'oauth:xw2i32iv4z1nqelne3xjjmxj7qfx9q',
    })
    bot4 = irc3.IrcBot.from_config(config)
    bot4.run(forever=False)

    config.update({
        'nick': 'obama_isa_muslim',
        'password': 'oauth:aj1ufoc4438urkm03rzgf8vvdriv8t',
    })
    bot5 = irc3.IrcBot.from_config(config)
    bot5.run(forever=False)
    print('serving')
    loop.run_forever()
    loop.close()

if __name__ == '__main__':
    main()
