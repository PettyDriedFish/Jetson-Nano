import tornado.ioloop
import tornado.web
import tornado.websocket
import getData
from kasa import SmartPlug
import asyncio

temp = getData.getCurrentTemp()
hum = getData.getCurrentHum()

# fanPlug = asyncio.run(SmartPlug("192.168.3.29").is_on)
# humidifierPlug = asyncio.run(SmartPlug("192.168.3.30").is_on)
# heaterPlug = asyncio.run(SmartPlug("192.168.3.31").is_on)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")

    def on_message(self, message):
        print("Received message:", message)
        if message == '1':
            writeMessage = f'Temperature now is {temp}'
        elif message == '2':
            writeMessage = f'Humidity now is {hum}'
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

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")
    tornado.ioloop.IOLoop.current().start()
