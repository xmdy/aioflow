from aiohttp import web

data = {
    'default': 'Hello!'
}

cont = 0


async def index(request):
    # global cont
    # cont += 1
    # print(cont)
    # k = 'asd'
    #
    # if k in data:
    #     res = data[k]
    # else:
    #     res = data['default']
    return web.Response(text='hello')

