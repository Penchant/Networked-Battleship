#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl, parse_qs
from src.Server.Ship import Ship

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        parsed_path = urlparse(self.path)
        request_id = parsed_path.path
        query = parse_qsl(self.path)
        print(parsed_path)
        print(query)
        self.wfile.write(bytes("Post!" + request_id, "utf8"))
        return

def run():
    print('starting Server...')

    destroyer = Ship(1,2,3,4,5, "Destroyer")
    print(Ship.location)
    print(Ship.location[0])
    print(Ship.name)
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http Server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running Server...')
    httpd.serve_forever()

    d = {}
    with open("Btest.txt") as f:
        x = 0
        y = 0
        for line in f:
            for c in line:
                d[(x, y)] = c
                y = y + 1
            x = x + 2
            y = 0
    print(d)

run()