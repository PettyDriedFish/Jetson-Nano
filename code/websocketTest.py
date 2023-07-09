import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")

    def on_message(self, message):
        print("Received message:", message)
        self.write_message("You sent: " + message)

    def on_close(self):
        print("WebSocket connection closed")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])
    app.listen(8000)
    print("WebSocket server started")
    tornado.ioloop.IOLoop.current().start()
