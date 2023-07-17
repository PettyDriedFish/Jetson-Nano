import kasa
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen
import getData
import setPlugs
import scheduleTH
import time
from kasa import SmartPlug
import json
import schedule
import datetime
import asyncio
import tracemalloc
tracemalloc.start()

globalData = {}  # 全局字典变量用于存储发送和接收的全部数据

# today_temperature = [0] * 24
# today_humidity = [0] * 24
#
# todayData = {
#     'today_temperature': today_temperature,
#     'today_humidity': today_humidity
# }

# class WebSocketHandler(tornado.websocket.WebSocketHandler):
#     def open(self):
#         print("WebSocket connection opened")
#         tornado.ioloop.IOLoop.current().spawn_callback(self.send_data)
#         self.update_globalData()
#
#     def on_message(self, message):
#         print("Received message:", message)
#         recevieData = json.loads(message)
#         fan_plug_status = recevieData['fan_plug_status']
#         humidifier_plug_status = recevieData['humidifier_plug_status']
#         heater_plug_status = recevieData['heater_plug_status']
#         self.min_temperature = recevieData['min_temperature']
#         self.max_temperature = recevieData['max_temperature']
#         self.min_humidity = recevieData['min_humidity']
#         self.max_humidity = recevieData['max_humidity']
#
#         asyncio.create_task(self.control_plug("192.168.3.29", fan_plug_status))
#         asyncio.create_task(self.control_plug("192.168.3.30", humidifier_plug_status))
#         asyncio.create_task(self.control_plug("192.168.3.31", heater_plug_status))
#
#     @gen.coroutine
#     def on_close(self):
#         print("WebSocket connection closed")
#         self.close(None)  # 添加这行代码来关闭流对象
#
#     # 获取plug状态
#     async def get_smartplug_state(self, ip_address):
#         try:
#             plug = SmartPlug(ip_address)
#             await plug.update()
#             return plug.is_on
#         except kasa.exceptions.SmartDeviceException:
#             return False  # 假设设备状态为关闭
#
#     # the data need to send
#     # 需要传输给手机的数据
#     async def send_data(self):
#         while self.ws_connection:
#             temperature = getData.getCurrentTemp()
#             humidity = getData.getCurrentHum()
#
#             fan_plug_state = await self.get_smartplug_state("192.168.3.29")
#             humidifier_plug_state = await self.get_smartplug_state("192.168.3.30")
#             heater_plug_state = await self.get_smartplug_state("192.168.3.31")
#
#             min_temperature = globalData.get('min_temperature', 24.00)
#             max_temperature = globalData.get('max_temperature', 27.00)
#             min_humidity = globalData.get('min_humidity', 45.00)
#             max_humidity = globalData.get('max_humidity', 55.00)
#
#             self.update_globalData()
#
#             sendData = {
#                 'temperature': temperature,
#                 'humidity': humidity,
#                 'fan_plug_state': fan_plug_state,
#                 'humidifier_plug_state': humidifier_plug_state,
#                 'heater_plug_state': heater_plug_state,
#                 'min_temperature': min_temperature,
#                 'max_temperature': max_temperature,
#                 'min_humidity': min_humidity,
#                 'max_humidity': max_humidity,
#                 # 'today_temperature': today_temperature,
#                 # 'today_humidity': today_humidity
#             }
#
#             message = json.dumps(sendData)
#
#             print(message)
#             if self.ws_connection:
#                 await self.write_message(message)
#
#             # 等待60秒后再次发送数据
#             await gen.sleep(30)
#
#     # 用于on_message中设置plug状态
#     # 如果plug_status为True且插座当前处于关闭状态则打开plug
#     # 如果plug_status为False且插座当前处于打开状态则关闭plug
#     async def control_plug(self, ip_address, plug_status):
#         plug = SmartPlug(ip_address)
#         await plug.update()
#
#         if plug_status and not plug.is_on:
#             await plug.turn_on()
#             print(f"Plug at {ip_address} turned on")
#         elif not plug_status and plug.is_on:
#             await plug.turn_off()
#             print(f"Plug at {ip_address} turned off")
#
#     # 全局数据更新
#     def update_globalData(self):
#         global data
#         data = {
#             'fan_plug_status': self.fan_plug_status,
#             'humidifier_plug_status': self.humidifier_plug_status,
#             'heater_plug_status': self.heater_plug_status,
#             'min_temperature': self.min_temperature,
#             'max_temperature': self.max_temperature,
#             'min_humidity': self.min_humidity,
#             'max_humidity': self.max_humidity
#             # 其他需要传输的数据
#         }

# 第二版
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        tornado.ioloop.IOLoop.current().spawn_callback(self.send_data)

    def on_message(self, message):
        print("Received message:", message)
        receiveData = json.loads(message)
        self.update_globalData(receiveData)
        self.control_plugs()

    @gen.coroutine
    def on_close(self):
        print("WebSocket connection closed")
        self.close(None)  # 添加这行代码来关闭流对象

    # 获取plug状态
    async def get_smartplug_state(self, ip_address):
        try:
            plug = SmartPlug(ip_address)
            await plug.update()
            return plug.is_on
        except kasa.exceptions.SmartDeviceException:
            return False  # 假设设备状态为关闭

    # the data need to send
    # 需要传输给手机的数据
    async def send_data(self):
        while self.ws_connection:
            # setPlugs.controlTH()

            temperature = getData.getCurrentTemp()
            humidity = getData.getCurrentHum()

            fan_plug_state = await self.get_smartplug_state("192.168.3.29")
            humidifier_plug_state = await self.get_smartplug_state("192.168.3.30")
            heater_plug_state = await self.get_smartplug_state("192.168.3.31")

            min_temperature = globalData.get('min_temperature', 24.00)
            max_temperature = globalData.get('max_temperature', 27.00)
            min_humidity = globalData.get('min_humidity', 45.00)
            max_humidity = globalData.get('max_humidity', 55.00)

            # 更新数据
            # scheduleTH.record_data()

            # 获取更新后的数据
            today_temperature = scheduleTH.data['today_temperature']
            today_humidity = scheduleTH.data['today_humidity']

            sendData = {
                'temperature': temperature,
                'humidity': humidity,
                'fan_plug_state': fan_plug_state,
                'humidifier_plug_state': humidifier_plug_state,
                'heater_plug_state': heater_plug_state,
                'min_temperature': min_temperature,
                'max_temperature': max_temperature,
                'min_humidity': min_humidity,
                'max_humidity': max_humidity,
                'today_temperature': today_temperature,
                'today_humidity': today_humidity
            }

            message = json.dumps(sendData)
            print(message)

            if self.ws_connection:
                await self.write_message(message)

            # 等待60秒后再次发送数据
            await gen.sleep(3600)

    # 用于on_message中设置plug状态
    # 如果plug_status为True且插座当前处于关闭状态则打开plug
    # 如果plug_status为False且插座当前处于打开状态则关闭plug
    async def control_plug(self, ip_address, plug_status):
        plug = SmartPlug(ip_address)
        await plug.update()

        if plug_status and not plug.is_on:
            await plug.turn_on()
            print(f"Plug at {ip_address} turned on")
        elif not plug_status and plug.is_on:
            await plug.turn_off()
            print(f"Plug at {ip_address} turned off")

    # 全局数据更新
    def update_globalData(self, receiveData):
        global globalData
        globalData = receiveData

    # 控制插座
    async def control_plugs(self):
        fan_plug_status = globalData.get('fan_plug_state', False)
        humidifier_plug_status = globalData.get('humidifier_plug_state', False)
        heater_plug_status = globalData.get('heater_plug_state', False)

        await self.control_plug("192.168.3.29", fan_plug_status)
        await self.control_plug("192.168.3.30", humidifier_plug_status)
        await self.control_plug("192.168.3.31", heater_plug_status)

    # def start_server(self):

    #     print("Executing websocketServer.py")
    #
    #     app = tornado.web.Application([
    #         (r"/websocket", WebSocketHandler),
    #     ])
    #     app.listen(8000)
    #     print("WebSocket server started")
    #     tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")

    # 启动Tornado的IOLoop循环
    tornado.ioloop.IOLoop.current().start()
