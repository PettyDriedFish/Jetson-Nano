import kasa
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen
import getData
import time
from kasa import SmartPlug
import json
import asyncio
import tracemalloc
tracemalloc.start()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        tornado.ioloop.IOLoop.current().spawn_callback(self.send_data)

    def on_message(self, message):
        print("Received message:", message)
        data = json.loads(message)
        fan_plug_status = data['fan_plug_status']
        humidifier_plug_status = data['humidifier_plug_status']
        heater_plug_status = data['heater_plug_status']

        asyncio.create_task(self.control_plug("192.168.3.29", fan_plug_status))
        asyncio.create_task(self.control_plug("192.168.3.30", humidifier_plug_status))
        asyncio.create_task(self.control_plug("192.168.3.31", heater_plug_status))

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
            temp = getData.getCurrentTemp()
            hum = getData.getCurrentHum()

            fan_plug_state = await self.get_smartplug_state("192.168.3.29")
            humidifier_plug_state = await self.get_smartplug_state("192.168.3.30")
            heater_plug_state = await self.get_smartplug_state("192.168.3.31")

            data = {
                'temperature': temp,
                'humidity': hum,
                'fan_plug_state': fan_plug_state,
                'humidifier_plug_state': humidifier_plug_state,
                'heater_plug_state': heater_plug_state
            }

            message = json.dumps(data)

            print(message)
            if self.ws_connection:
                await self.write_message(message)

            # 等待60秒后再次发送数据
            await gen.sleep(10)

    async def control_plug(self, ip_address, plug_status):
        plug = SmartPlug(ip_address)
        await plug.update()

        if plug_status and not plug.is_on:
            await plug.turn_on()
            print(f"Plug at {ip_address} turned on")
        elif not plug_status and plug.is_on:
            await plug.turn_off()
            print(f"Plug at {ip_address} turned off")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")
    tornado.ioloop.IOLoop.current().start()

