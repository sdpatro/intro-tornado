__author__ = 'sdpatro'
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

from signup import SignUpHandler
from login import LoginHandler
from DB import DBHandler

import torndb


class MainHandler(RequestHandler):
    def get(self):
        self.write('<h1>Welcome</h1> <br/> Sign up <a href="%s">here</a> and log in <a href="%s">here</a>' % (
            self.reverse_url("signup"),
            self.reverse_url("login")))


if __name__ == "__main__":
    app = Application([
        url(r"/", MainHandler),
        url(r"/signup", SignUpHandler.SignUpHandler, name="signup"),
        url(r"/login", LoginHandler.LoginHandler, name="login"),
        url(r"/db", DBHandler.DBHandler, name="db")])

    app.listen(8888)
    IOLoop.current().start()
