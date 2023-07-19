import asyncio
import threading
from datetime import time

import tornado

import scheduleTH
import setPlugs
import websocketServer

# 创建锁对象
lock = threading.Lock()


# def run_websocket_server():
#     # 获取锁
#     lock.acquire()
#     try:
#         print('Thread 2 - Entered run_websocket_server')
#         print('Thread 2 - Entered run_websocket_server')
#         app = tornado.web.Application([
#             (r"/websocket", websocketServer.WebSocketHandler),
#         ])
#         app.listen(8000)
#         print("WebSocket server started")
#         tornado.ioloop.IOLoop.current().start()
#     finally:
#         # 释放锁
#         if lock.locked():
#             lock.release()
#             print('Thread 2 - Lock released')


def run_set_plugs():
    # 获取锁
    lock.acquire()
    try:
        print('Thread 1 - Entered run_set_plugs\n')
        print('Thread 1 - Entered run_set_plugs\n')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(setPlugs.controlTH())
    finally:
        # 释放锁
        if lock.locked():
            lock.release()
            print('Thread 1 - Lock released\n')

def run_websocket_server():
    # 获取锁
    lock.acquire()
    try:
        print('Thread 2 - Entered run_websocket_server\n')
        print('Thread 2 - Entered run_websocket_server\n')
        app = tornado.web.Application([
            (r"/websocket", websocketServer.WebSocketHandler),
        ])
        app.listen(8000)
        print("WebSocket server started")
        tornado.ioloop.IOLoop.current().start()
        # WebSocket server关闭后释放锁
        if lock.locked():
            lock.release()
            print('Thread 2 - Lock released\n')
    except Exception as e:
        print('Exception in run_websocket_server:', str(e))
        if lock.locked():
            lock.release()
            print('Thread 2 - Lock released\n')

def run_scheduleTH():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(scheduleTH.run_schedule())
    # # 获取锁
    # lock.acquire()
    # try:
    #     print('Thread 3 - Entered run_scheduleTH\n')
    #     print('Thread 3 - Entered run_scheduleTH\n')
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     loop.run_until_complete(scheduleTH.run_schedule())
    # finally:
    #     # 释放锁
    #     if lock.locked():
    #         lock.release()
    #         print('Thread 3 - Lock released\n')



# 创建并启动线程
thread1 = threading.Thread(target=run_set_plugs)
thread2 = threading.Thread(target=run_websocket_server)
# thread3 = threading.Thread(target=run_scheduleTH)
thread1.start()
thread2.start()
# thread3.start()

# run_set_plugs()
# 运行scheduleTH
asyncio.run(run_scheduleTH())

# 运行 setPlugs 和 scheduleTH
# asyncio.gather(
#     run_set_plugs(),
#     run_scheduleTH());


# 等待线程结束
thread1.join()
thread2.join()
# thread3.join()

