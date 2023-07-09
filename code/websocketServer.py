import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen
import getData
import time
from kasa import SmartPlug
import asyncio
import tracemalloc
tracemalloc.start()

# temp = getData.getCurrentTemp()
# hum = getData.getCurrentHum()

# fanPlug = asyncio.run(SmartPlug("192.168.3.29").is_on)
# humidifierPlug = asyncio.run(SmartPlug("192.168.3.30").is_on)
# heaterPlug = asyncio.run(SmartPlug("192.168.3.31").is_on)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        tornado.ioloop.IOLoop.current().spawn_callback(self.send_data)
        # self.send_temperature_humidity()

    def on_message(self, message):
        print("Received message:", message)
        # self.send_data()  # 收到任何消息时都发送一次消息
        # if message == '1':
        #     writeMessage = f'Temperature now is temp'
        # elif message == '2':
        #     writeMessage = f'Humidity now is hum'
        # # elif message == '3':
        # #     writeMessage = f'fanPlug now is {fanPlug}'
        # # elif message == '4':
        # #     writeMessage = f'humidifierPlug now is {humidifierPlug}'
        # # elif message == '5':
        # #     writeMessage = f'heaterPlug now is {heaterPlug}'
        # else:
        #     writeMessage = message
        # self.write_message(writeMessage)

    @gen.coroutine
    def on_close(self):
        print("WebSocket connection closed")
        self.close(None)  # 添加这行代码来关闭流对象

    def send_temperature_humidity(self):
        while True:
            temp = getData.getCurrentTemp()
            hum = getData.getCurrentHum()

            writeMessage = f'Temperature now is {temp}, Humidity now is {hum}'
            print(writeMessage)
            self.write_message(writeMessage)

            # wait for 60 seconds
            time.sleep(60)

    async def get_smartplug_state(self, ip_address):
        plug = SmartPlug(ip_address)
        await plug.update()
        return plug.is_on

    async def send_data(self):
        while True:
            temp = getData.getCurrentTemp()
            hum = getData.getCurrentHum()

            # fanPlug = asyncio.run(SmartPlug("192.168.3.29").update())
            # humidifierPlug = asyncio.run(SmartPlug("192.168.3.30").update())
            # heaterPlug = asyncio.run(SmartPlug("192.168.3.31").update())
            #
            # fan_plug_state = fanPlug.is_on
            # humidifier_plug_state = humidifierPlug.is_on
            # heater_plug_state = heaterPlug.is_on

            fan_plug_state = await self.get_smartplug_state("192.168.3.29")
            humidifier_plug_state = await self.get_smartplug_state("192.168.3.30")
            heater_plug_state = await self.get_smartplug_state("192.168.3.31")

            message = f'Temperature now is {temp}, Humidity now is {hum}\n'
            message += f'Fan Plug is {"on" if fan_plug_state else "off"}\n'
            message += f'Humidifier Plug is {"on" if humidifier_plug_state else "off"}\n'
            message += f'Heater Plug is {"on" if heater_plug_state else "off"}'

            print(message)
            await self.write_message(message)

            # 等待60秒后再次发送数据
            time.sleep(10)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")
    tornado.ioloop.IOLoop.current().start()
