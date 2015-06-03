__author__ = 'sdpatro'
from tornado.web import RequestHandler
import torndb


class DBHandler(RequestHandler):
    def get(self):
        self.write("Database")

    def post(self):

        fullName = self.get_body_argument("name")
        userName = self.get_body_argument("username")
        password = self.get_body_argument("password")
        emailID = self.get_body_argument("emailid")
        db = torndb.Connection("localhost", "testdb", "root", "root")
        queryResult = db.query("SELECT userName FROM clients WHERE userName=\"" + userName + "\";")

        if len(queryResult) > 0:
            self.write("User already exists, <a href=%s>try again.</a>" % "/signup")
        else:
            try:
                db.insert("INSERT INTO clients VALUES(\"" + fullName + "\",\"" + userName + "\",\"" + password + "\",\"" + emailID+"\");")
                self.write("Account made, go to <a href=%s>login.</a>" % "/login")
            except:
                self.write("Something occurred, <a href=%s>try again.</a>" % "/signup")