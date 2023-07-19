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
        # 60秒后调用函数释放锁
        tornado.ioloop.IOLoop.current().call_later(60, self.release_lock)

    def on_message(self, message):
        print("Received message:", message)
        receiveData = json.loads(message)
        fan_plug_state = receiveData['fan_plug_state']
        humidifier_plug_state = receiveData['humidifier_plug_state']
        heater_plug_state = receiveData['heater_plug_state']

        asyncio.create_task(self.control_plug("192.168.3.29", fan_plug_state))
        asyncio.create_task(self.control_plug("192.168.3.30", humidifier_plug_state))
        asyncio.create_task(self.control_plug("192.168.3.31", heater_plug_state))

        # 更新全局数据
        self.update_globalData(receiveData)

        # print("Received message:", message)
        # receiveData = json.loads(message)
        # # 通过将对main模块的导入放在函数内部，可以避免循环导入问题
        # from main import lock
        # # 获取锁
        # lock.acquire()
        # # self.update_globalData(receiveData)
        # try:
        #     fan_plug_state = receiveData['fan_plug_state']
        #     humidifier_plug_state = receiveData['humidifier_plug_state']
        #     heater_plug_state = receiveData['heater_plug_state']
        #
        #     asyncio.create_task(self.control_plug("192.168.3.29", fan_plug_state))
        #     asyncio.create_task(self.control_plug("192.168.3.30", humidifier_plug_state))
        #     asyncio.create_task(self.control_plug("192.168.3.31", heater_plug_state))
        #
        #     # 更新全局数据
        #     self.update_globalData(receiveData)
        # finally:
        #     # 释放锁
        #     if lock.locked():
        #         lock.release()
        #         print("on_message： Lock released")
        # self.close()


    @gen.coroutine
    def on_close(self):
        print("WebSocket connection closed")
        # 关闭流对象
        self.close()
        self.stream.close()
        # 通过将对main模块的导入放在函数内部，可以避免循环导入问题
        from main import lock
        # 释放锁
        if lock.locked():
            lock.release()
            print("on_close： Lock released")
        print("WebSocket connection closed")

    def release_lock(self):
        # 获取锁
        from main import lock
        if lock.locked():
            lock.release()
            print("release_lock： Lock released")

    async def get_smartplug_state(self, ip_address):
        try:
            plug = SmartPlug(ip_address)
            await plug.update()
            return plug.is_on
        except kasa.exceptions.SmartDeviceException:
            return False  # 假设设备状态为关闭

    async def send_data(self):
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

        # import scheduleTH

        # 获取更新后的数据
        today_temperature = self.get_today_temperature()
        today_humidity = self.get_today_humidity()

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

    def get_today_temperature(self):
        # import scheduleTH
        # 获取更新后的数据
        today_temperature = scheduleTH.data['today_temperature']
        return today_temperature

    def get_today_humidity(self):
        # import scheduleTH
        # 获取更新后的数据
        today_humidity = scheduleTH.data['today_humidity']
        return today_humidity

# if __name__ == "__main__":
#     app = tornado.web.Application([
#         (r"/websocket", WebSocketHandler),
#     ])
#     app.listen(8000)
#     print("WebSocket server started")
#     tornado.ioloop.IOLoop.current().start()
