__author__ = 'sdpatro'
from tornado.web import RequestHandler
import torndb


class LoginHandler(RequestHandler):
    def get(self):
        self.render("Login.html", title="Log in")

    def post(self):
        userName = self.get_body_argument("username")
        password = self.get_body_argument("password")
        db = torndb.Connection("localhost", "testdb", "root", "root")
        queryResult = db.query("SELECT userName,password FROM clients WHERE userName=\"" + userName + "\";")

        if len(queryResult) == 0:
            self.write("No such username, <a href=%s>try again.</a>" % "/login")
        else:
            for user in queryResult:
                if user.password != password:
                    self.write("Wrong password, <a href=%s>try again.</a>" % "/login")
                else:
                    self.set_secure_cookie("user", self.get_argument("username"))
                    self.redirect(self.reverse_url("landing"))
