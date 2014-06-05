from BaseHTTPServer import BaseHTTPRequestHandler
import threading
import argparse
import cgi
from pprint import pprint
import json
import urllib
import os
from Router import *
from Controllers import *

class HTTPRequestHandler(BaseHTTPRequestHandler):
    router = Router()

    def do_GET(self):
        self.root = os.path.dirname(os.path.abspath(__file__)) + "/../../"
        routeDetails = self.router.getRouteDetails(self.path)
        self.execute(routeDetails)

    def execute(self, actions):
        print actions
        constructor = globals()[actions['controller']]
        obj = constructor(self, self.root)
        result = getattr(obj, actions['action'])(actions['location'], actions)

        
    # def do_OPTIONS(self):
    #     self.CommonFunc()
    # def do_POST(self):
    #     self.CommonFunc()

    # def CommonFunc(self):
    #     k = self.path[self.path.index("=") + 1:]
    #     data = json.loads(urllib.unquote(k).decode('utf8'))
    #     db = DBAccess()
    #     popular = db.execs(data)

    #     #finish response send OK
    #     self.send_response(200)
    #     self.send_header("Access-Control-Allow-Origin", "*")
    #     self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    #     self.send_header("Access-Control-Allow-Headers", "content-type")
    #     self.send_header("Content-Type", "text/plain");
    #     self.end_headers()
    #     # Send the html message
    #     self.wfile.write(popular)