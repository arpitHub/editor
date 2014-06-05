from pprint import pprint
import re, os
import routes

class Router:
    routes = {
        "/": [ "home", "Views/index.html"],
        "/js/{file}": ["javascript", "js/"]
    }

    root = os.path.dirname(os.path.abspath(__file__)) + "/../../"
    mapper = routes.Mapper()

    def __init__(self):
        for route in self.routes:
            self.mapper.connect(self.routes[route][0], )


    def getFileContent(self, path):
        for route in self.routes.keys():
            print route
            print path
            result = re.match(r""+ route +"", path)
            if result is not None:
                print result.group(0)
                return self.root + self.routes[route][0]

            print "-----------------"

