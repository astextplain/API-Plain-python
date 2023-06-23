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

        # Prepare response
        response_data = {
            'message': 'Hello, World!'
        }
        response_body = json.dumps(response_data)

        self.wfile.write(response_body.encode())

    def do_POST(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Get the content length from request headers
        content_length = int(self.headers['Content-Length'])

        # Read the request body
        request_body = self.rfile.read(content_length)

        received_data = json.loads(request_body)
        if 'key1' in received_data:
            value1 = received_data['key1']

        if value1 == 'example':
            result = value1.upper()
        else:
            result = value1.lower()
        received_data['key1'] = result

        response_data = {
            'message': 'POST request received',
            'data': received_data
        }
        response_body = json.dumps(response_data)

        self.wfile.write(response_body.encode())

    def do_PUT(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Get the content length
        content_length = int(self.headers['Content-Length'])

        # Read request body
        request_body = self.rfile.read(content_length)

        # Process request
        received_data = json.loads(request_body)

        response_data = {
            'message': 'PUT request received',
            'data': received_data
        }
        response_body = json.dumps(response_data)

        self.wfile.write(response_body.encode())

    def do_DELETE(self):

        self.send_response(200)

        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])

        # Read the request body
        request_body = self.rfile.read(content_length)
        received_data = json.loads(request_body)
        response_data = {
            'message': 'DELETE request received',
            'data': received_data
        }
        response_body = json.dumps(response_data)
        self.wfile.write(response_body.encode())


HOST = 'localhost'
PORT = 8000

# Create the server
with socketserver.TCPServer((HOST, PORT), MyRequestHandler) as server:
    print(f'Server started at {HOST}:{PORT}')

    server.serve_forever()
