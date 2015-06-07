__author__ = 'sdpatro'
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.httpserver import HTTPServer

from signup import SignUpHandler
from login import LoginHandler
from DB import DBHandler
from landing import LandingHandler

import random


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("landing")
            return
        self.write('<h1>Welcome</h1> <br/> Sign up <a href="%s">here</a> and log in <a href="%s">here</a>' % (
            self.reverse_url("signup"),
            self.reverse_url("login")))


if __name__ == "__main__":
    app = Application([
        url(r"/", MainHandler),
        url(r"/signup", SignUpHandler.SignUpHandler, name="signup"),
        url(r"/login", LoginHandler.LoginHandler, name="login"),
        url(r"/landing", LandingHandler.LandingHandler, name="landing"),
        url(r"/db", DBHandler.DBHandler, name="db")], cookie_secret=str(random.randrange(0, 10000000)))

    server = HTTPServer(app, xheaders=True)
    server.bind(8888)
    server.start(0)
    IOLoop.current().start()
