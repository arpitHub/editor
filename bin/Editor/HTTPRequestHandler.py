from BaseHTTPServer import BaseHTTPRequestHandler
import threading
import argparse
import cgi
from pprint import pprint
import json
import urllib
import os
from Router import *

class HTTPRequestHandler(BaseHTTPRequestHandler):

    indexFIle = "index.html"
    routes = {
        "/": ["Views/index.html", 'text/html'],
        "/index.html": ["index.html", 'text/html'],
        "/js": [ "js/" ]
    }
    router = Router()

    def do_GET(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        content = ""
        ctype = 'text/html'
        if self.path in self.routes :
            # path = directory + "/../../" + self.routes[self.path][0]
            path = self.router.getFileContent(self.path)
            with open(path, 'r') as content_file:
                content = content_file.read()
            ctype = self.routes[self.path][1]
        else:
            content = "<h2>No Route Found</h2>"
            ctype = 'text/html'
        self.send_response(200)
        self.send_header('Content-Type', ctype)
        self.end_headers()

        self.wfile.write(content)

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