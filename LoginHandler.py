__author__ = 'sdpatro'
from tornado.web import RequestHandler


class LoginHandler(RequestHandler):
    def get(self):
        self.render("Login.html", title="Log in")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))
