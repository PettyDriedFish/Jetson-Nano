import kasa
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen
import getData
import scheduleTH
import time
from kasa import SmartPlug
import json
import asyncio
import tracemalloc
tracemalloc.start()

globalData = {}  # 全局字典变量用于存储发送和接收的全部数据

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        tornado.ioloop.IOLoop.current().spawn_callback(self.send_data)

    def on_message(self, message):
        print("Received message:", message)
        receiveData = json.loads(message)
        # self.update_globalData(receiveData)
        # self.set_plugs()
        # print("Received message:", message)
        fan_plug_state = receiveData['fan_plug_state']
        humidifier_plug_state = receiveData['humidifier_plug_state']
        heater_plug_state = receiveData['heater_plug_state']

        asyncio.create_task(self.control_plug("192.168.3.29", fan_plug_state))
        asyncio.create_task(self.control_plug("192.168.3.30", humidifier_plug_state))
        asyncio.create_task(self.control_plug("192.168.3.31", heater_plug_state))

        self.update_globalData(receiveData)

    @gen.coroutine
    def on_close(self):
        print("WebSocket connection closed")
        self.close(None)  # 添加这行代码来关闭流对象

    async def get_smartplug_state(self, ip_address):
        try:
            plug = SmartPlug(ip_address)
            await plug.update()
            return plug.is_on
        except kasa.exceptions.SmartDeviceException:
            return False  # 假设设备状态为关闭

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
        # while self.ws_connection:
        #     temp = getData.getCurrentTemp()
        #     hum = getData.getCurrentHum()
        #
        #     fan_plug_state = await self.get_smartplug_state("192.168.3.29")
        #     humidifier_plug_state = await self.get_smartplug_state("192.168.3.30")
        #     heater_plug_state = await self.get_smartplug_state("192.168.3.31")
        #
        #     data = {
        #         'temperature': temp,
        #         'humidity': hum,
        #         'fan_plug_state': fan_plug_state,
        #         'humidifier_plug_state': humidifier_plug_state,
        #         'heater_plug_state': heater_plug_state
        #     }
        #
        #     message = json.dumps(data)
        #
        #     print(message)
        #     if self.ws_connection:
        #         await self.write_message(message)
        #
        #     # 等待60秒后再次发送数据
        #     await gen.sleep(10)

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
    async def set_plugs(self):
        fan_plug_status = globalData.get('fan_plug_state', False)
        humidifier_plug_status = globalData.get('humidifier_plug_state', False)
        heater_plug_status = globalData.get('heater_plug_state', False)

        await self.control_plug("192.168.3.29", fan_plug_status)
        await self.control_plug("192.168.3.30", humidifier_plug_status)
        await self.control_plug("192.168.3.31", heater_plug_status)


# if __name__ == "__main__":
#     app = tornado.web.Application([
#         (r"/websocket", WebSocketHandler),
#     ])
#     app.listen(8000)
#     print("WebSocket server started")
#     tornado.ioloop.IOLoop.current().start()