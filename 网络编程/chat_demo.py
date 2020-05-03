import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
 
    def open(self):
        pass
 
    def on_message(self, message):
        print(message)
        self.write_message(u"Your message was: "+message)
 
    def on_close(self):
        pass
 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/ws', WebSocketHandler)
        ]
        # settings = { "template_path": "."}
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)
 
if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()