__author__ = 'sdpatro'
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

class MainHandler(RequestHandler):
    def get(self):
        self.write('<a href="%s">form</a>' %
                   self.reverse_url("form"))

if __name__ == "__main__":
    app = Application([
        url(r"/", MainHandler)])

    app.listen(8888)
    IOLoop.current().start()
