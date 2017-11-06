from aiohttp import web
import redis


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "hello, " + name
    r.publish('spam', name)
    return web.Response(text=text)

r = redis.Redis()
app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)
web.run_app(app, host='127.0.0.1', port=8080)

