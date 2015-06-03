__author__ = 'sdpatro'
from tornado.web import RequestHandler

class SignUpHandler(RequestHandler):
    def get(self):
        self.render("SignUp.html", title="Sign up")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.reverse_url("db"))