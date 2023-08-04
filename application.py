from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'This is the text response from the server.')

def run():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

run()
