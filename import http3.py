import http.server
import socketserver


class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # index.html file
        try:
            with open('index.html', 'rb') as file:
                response_body = file.read()
        except FileNotFoundError:
            response_body = b'File not found'

        self.wfile.write(response_body)


HOST = 'localhost'
PORT = 8002
with socketserver.TCPServer((HOST, PORT), handler) as server:
    print(f'Server started at {HOST}:{PORT}')

    server.serve_forever()
