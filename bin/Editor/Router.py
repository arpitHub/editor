from pprint import pprint
import re, os
from routes import Mapper

class Router:
    routes = {
        "/":          ["home", "Views/index.html", "HomePage", "index"],
        "/js/{file:.*}": ["javascript", "js/", "HomePage", "jsAction"],
        "/ace-builds/{file:.*}": ["javascript", "ace-builds/", "HomePage", "jsAction"]
    }

    root = os.path.dirname(os.path.abspath(__file__)) + "/../../"
    mapper = Mapper()

    def __init__(self):
        for route in self.routes:
            details = self.routes[route]
            self.mapper.connect(details[0], route, controller=details[2], action=details[3], location=details[1])


    def getRouteDetails(self, path):
        result = self.mapper.match(path)
        return result
