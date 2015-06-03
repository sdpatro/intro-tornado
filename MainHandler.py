__author__ = 'sdpatro'
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
import SignUpHandler
import LoginHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write('<h1>Welcome</h1> <br/> Sign up <a href="%s">here</a> and log in <a href="%s">here</a>' % (
            self.reverse_url("signup"),
            self.reverse_url("login")))

if __name__ == "__main__":
    app = Application([
        url(r"/", MainHandler),
        url(r"/signup", SignUpHandler.SignUpHandler, name="signup"),
        url(r"/login", LoginHandler.LoginHandler, name="login")])

    app.listen(8888)
    IOLoop.current().start()
