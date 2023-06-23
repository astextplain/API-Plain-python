import http.server
import socketserver
import json


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status code
        self.send_response(200)

        # Set response headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {
            'message': 'Hello, World!'
        }
        response_body = json.dumps(response_data)

        # Send the response
        self.wfile.write(response_body.encode())


# server settings
HOST = 'localhost'
PORT = 8000

# Create the server
with socketserver.TCPServer((HOST, PORT), MyRequestHandler) as server:
    print(f'Server started at {HOST}:{PORT}')
    # Start the server
    server.serve_forever()
