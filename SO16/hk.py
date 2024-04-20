import http.server
import socketserver
from urllib.parse import parse_qs

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class EchoHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <head><title>Echo Server</title></head>
                <body>
                    <h1>Enter a message:</h1>
                    <form method="POST" action="/echo">
                        <input type="text" name="message">
                        <input type="submit" value="Submit">
                    </form>
                </body>
                </html>
            ''')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <head><title>404 Not Found</title></head>
                <body>
                    <h1>404 Not Found</h1>
                    <a href="/">Return to form</a>
                </body>
                </html>
            ''')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        message = params['message'][0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'''
            <html>
            <head><title>Message Echoed</title></head>
            <body>
                <h1>Message Echoed:</h1>
                <p>{message}</p>
                <a href="/">Return to form</a>
            </body>
            </html>
        '''.encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), EchoHandler) as httpd:
        print(f"Server started on port {PORT}")
        httpd.serve_forever()
