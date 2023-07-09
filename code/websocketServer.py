import tornado.ioloop
import tornado.web
import tornado.websocket
import getData
import time
from kasa import SmartPlug
import asyncio

# temp = getData.getCurrentTemp()
# hum = getData.getCurrentHum()

# fanPlug = asyncio.run(SmartPlug("192.168.3.29").is_on)
# humidifierPlug = asyncio.run(SmartPlug("192.168.3.30").is_on)
# heaterPlug = asyncio.run(SmartPlug("192.168.3.31").is_on)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        self.send_temperature_humidity()  # 初始连接时立即发送一次温湿度消息

    def on_message(self, message):
        print("Received message:", message)
        self.send_temperature_humidity()  # 收到任何消息时都发送一次温湿度消息
        if message == '1':
            writeMessage = f'Temperature now is temp'
        elif message == '2':
            writeMessage = f'Humidity now is hum'
        # elif message == '3':
        #     writeMessage = f'fanPlug now is {fanPlug}'
        # elif message == '4':
        #     writeMessage = f'humidifierPlug now is {humidifierPlug}'
        # elif message == '5':
        #     writeMessage = f'heaterPlug now is {heaterPlug}'
        else:
            writeMessage = message
        self.write_message(writeMessage)

    def on_close(self):
        print("WebSocket connection closed")

    def send_temperature_humidity(self):
        while True:
            temp = getData.getCurrentTemp()
            hum = getData.getCurrentHum()

            writeMessage = f'Temperature now is {temp}, Humidity now is {hum}'
            print(writeMessage)
            self.write_message(writeMessage)

            # wait for 60 seconds
            time.sleep(60)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")
    tornado.ioloop.IOLoop.current().start()
