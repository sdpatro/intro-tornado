__author__ = 'sdpatro'
from tornado.web import RequestHandler, Application, url
import torndb

class LandingHandler(RequestHandler):
    def get(self):
        name = self.get_secure_cookie("user")
        db = torndb.Connection("localhost", "testdb", "root", "root")
        queryResult = db.query("SELECT * FROM products WHERE userName=\"" + str(name) + "\";")
        print(queryResult)
        self.render("landing.html", title="Logged in.", items=queryResult)

    def post(self):
        pass

