#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl, parse_qs
from src.Server.Ship import Ship, ShipType

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
        query = parse_qsl(parsed_path.query)
        print(parsed_path)
        print(parsed_path.query)
        print(query)

        status = "Hit " if True else "Miss"

        self.wfile.write(bytes("Accept" + "", "utf8"))
        return

def run():
    print('starting Battleship...')

    destroyer = Ship(1,2,3,4, ShipType.Destroyer)
    print(Ship.location)
    print(Ship.location[0])
    print(Ship.shipType.name)

    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running Battleship...')
    httpd.serve_forever()

run()