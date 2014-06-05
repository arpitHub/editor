
class HomePage:
    appRoot = ""
    serv = None
    ctype = {
        'HTML': "text/html",
        'JS': 'text/javascript'
    }

    def __init__(self, serv, root):
        self.serv = serv
        self.appRoot = root

    def index(self, location, options=None):
        location = self.appRoot + location
        with open(location, 'r') as content_file:
            content = content_file.read()

        self.serv.send_response(200)
        self.serv.send_header('Content-Type', self.ctype['HTML'])
        self.serv.end_headers()

        self.serv.wfile.write(content)

    def jsAction(self, location, options=None):
        location = self.appRoot + location + options['file']
        with open(location, 'r') as content_file:
            content = content_file.read()

        self.serv.send_response(200)
        self.serv.send_header('Content-Type', self.ctype['JS'])
        self.serv.end_headers()

        self.serv.wfile.write(content)

