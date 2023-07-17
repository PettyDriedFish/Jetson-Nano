import threading

import tornado

import websocketServer

# 创建锁对象
lock = threading.Lock()

def run_websocket_server():
    # 获取锁
    lock.acquire()
    try:
        app = tornado.web.Application([
            (r"/websocket", websocketServer.WebSocketHandler),
        ])
        app.listen(8000)
        print("WebSocket server started")
        tornado.ioloop.IOLoop.current().start()
    finally:
        # 释放锁
        lock.release()

# 创建并启动线程
thread = threading.Thread(target = run_websocket_server)
thread.start()

# 等待线程结束
thread.join()

# 打印最终的全局变量
print("Global Data:", websocketServer.globalData)
