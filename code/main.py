import threading
import asyncio
import time

import tornado

import scheduleTH
# from scheduleTH import ScheduleTH
import setPlugs
import websocketServer

# def run_schedule():
#     ScheduleTH.start_schedule()
    # while True:
    #     scheduleTH.schedule.run_pending()
    #     time.sleep(1)  # 添加延迟

# def run_set_plugs():
#     tornado.ioloop.IOLoop.current().run_sync(setPlugs.controlTH)
#
#     # asyncio.create_task(setPlugs.controlTH())
#
# def run_websocket_server():
#     # websocketServer.start_server()
#     server = websocketServer.WebSocketHandler()
#     server.start_server()

# if __name__ == "__main__":
#     # 创建 Tornado 应用程序对象，并将 application 参数设置为 None
#     app = tornado.web.Application([
#         (r"/websocket", websocketServer.WebSocketHandler),
#     ])
#     app.listen(8000)
#     print("WebSocket server started")
#     tornado.ioloop.IOLoop.current().start()

    # # 创建线程并运行各个文件
    # set_plugs_thread = threading.Thread(target=run_set_plugs)
    # websocket_server_thread = threading.Thread(target=websocketServer.WebSocketHandler().start_server)
    #
    # # 创建 ScheduleTask 实例并运行定时任务
    # schedule_task = scheduleTH.ScheduleTask()
    # schedule_thread = threading.Thread(target=schedule_task.start_schedule)
    #
    # # 启动线程
    # set_plugs_thread.start()
    # websocket_server_thread.start()
    # schedule_thread.start()
    #
    # # 等待线程结束
    # set_plugs_thread.join()
    # websocket_server_thread.join()
    # schedule_thread.join()

    # # 创建线程并运行各个文件
    # # schedule_thread = threading.Thread(target=run_schedule)
    # set_plugs_thread = threading.Thread(target=run_set_plugs)
    # websocket_server_thread = threading.Thread(target=run_websocket_server)
    #
    # # 启动线程
    # # schedule_thread.start()
    # set_plugs_thread.start()
    # websocket_server_thread.start()
    #
    # # 等待线程结束
    # # schedule_thread.join()
    # set_plugs_thread.join()
    # websocket_server_thread.join()