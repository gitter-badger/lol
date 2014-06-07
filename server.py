import http.server
import socketserver

def serve(port):
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", port), Handler)

    httpd.serve_forever()
