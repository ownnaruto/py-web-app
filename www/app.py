import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

# GET请求的处理函数
def index(request):
    return web.Response(body = b'<h1>Awesome</h1>',headers = {'content-type':'text/html'})


def init(): # web app服务器初始化
   
   # 创建web服务器，并将处理函数注册到应用路径(app.router)
    app = web.Application() 
    app.router.add_route('GET','/',index)

    """
    注释为 lxf 教程的写法，但过于老旧

    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000) # 用协程创建监听服务，返回的srv也是一个协程
    """
    # 在给定主机，端口下运行，这样写更好理解
    web.run_app(app,host = '127.0.0.1',port = 9000)
    logging.info('server stated at http://127.0.0.1:9000...')

init()


