from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import redis

PORT = int(os.environ.get('HTTP_PORT'))
REDIS_SERVER = os.environ.get('REDIS_SERVER')

cacheServer = redis.Redis(host=REDIS_SERVER, port=6379, db=0)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        count = cacheServer.get('hit-counter')
        print("Server VERSION 2 started at localhost:" + str(count))
        self.wfile.write(bytes('Hello, world! This is hit number %s' % str(count), 'utf8'))
        cacheServer.incr('hit-counter')


httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)

print("Server VERSION 2 started at localhost:" + str(PORT))
httpd.serve_forever()


