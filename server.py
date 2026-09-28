import http.server
import socketserver
import os
import sys

# Render assigns a dynamic port via environment variable $PORT (default to 8080 locally)
PORT = int(os.environ.get('PORT', 8080))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================")
        print("PRIME STUDY ABROAD PORTAL - WEB SERVER")
        print("Official Agent: Moaaz Enany (Founder & Product Director)")
        print(f"Listening on Port: {PORT}")
        print(f"Directory:         {DIRECTORY}")
        print("==================================================")
        sys.stdout.flush()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")
