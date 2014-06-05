import Editor
from BaseHTTPServer import HTTPServer

port = 1551
ip =  'localhost'

try:
    server = HTTPServer(('', port), Editor.HTTPRequestHandler)
    print 'Started httpserver on port ' , port
   
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
   print '^C received, shutting down the web server'
   server.socket.close()