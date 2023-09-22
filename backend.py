import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
'''
This is a simple Websockets Echo server that uses the Tornado websockets handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it receives.
Headers in the message are output to the terminal for debugging purposes.
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
            # Access headers received in the WebSocket request
            headers = self.request.headers
            print("WebSocket headers received:", headers)

      
    def on_message(self, message):
        print ('message received:  ',message)
        #print ('sending back message: ' % message[::-1])
        self.write_message(message)
 
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('** Websockets Server Started at **' ,myIP)
    tornado.ioloop.IOLoop.instance().start()
