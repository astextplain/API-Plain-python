import http.server
import socketserver
import json


class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # responese
        self.send_response(200)
        # set response
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # create response
        if self.path == '/':
            # show homepage
            response_body = '<h1>Welcome<h1>'
        elif self.path == '/about':

            response_body = '<h1>About Us</h1><p>We are a company providing...</p>'
        else:

            response_body = '<h1>404 - Page Not Found</h1>'
        self.wfile.write(response_body.encode())


# server setting
HOST = 'localhost'
PORT = 8001
# create server
with socketserver.TCPServer((HOST, PORT), handler)as Serve:
    print(f'Server started at {HOST}:{PORT}')

    Serve.serve_forever()
