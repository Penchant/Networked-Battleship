#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl, parse_qs
from src.Server.Ship import Ship, ShipType

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Doesn't do anything with posted data

        parsed_path = urlparse(self.path)
        query = parse_qsl(parsed_path.query)

        x = int(query[0][1])
        y = int(query[1][1])

        print(str(x) + str(y))

        if( x > 9  or x < 0 or y > 9 or y < 0):
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print("hello")
            return

        inShips(x,y)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("hit=" + status + "&sunk=" + str(sunk), "utf8"))
        return
def inShips(x, y):
    global status
    global sunk
    for ship in Ships:
        if (ship.__contains__(ship, (x, y))):
            status = "1"
            sunk = 1 if ship.sunk(ship) else 0
        else:
            status = "0"
            sunk = 0
def run():
    print('starting Battleship...')

    global status
    global sunk
    global Ships
    Ships = [Ship] * 1

    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

    print('running Battleship...')


    d2 = {}
    with open("BlankTest.txt") as f:
        x = 0
        y = 0
        for line in f:
            for c in line:
                d2[(x, y)] = c
                y = y + 1
                if y == 10:
                    break
            x = x + 1
            if x == 10:
                break
            y = 0
    print(d2)


    boardC = ""
    cntCheckx = 0
    while cntCheckx < 10:
        cntChecky = 0
        while cntChecky < 10:
            boardC += (d2[(cntCheckx,cntChecky)])
            cntChecky = cntChecky + 1
        boardC += "\n"
        cntCheckx = cntCheckx + 1
    print(boardC)



    d1 = {}
    with open("Btest.txt") as f:
        x = 0
        y = 0
        for line in f:
            for c in line:
                d1[(x, y)] = c
                y = y + 1
                if y == 10:
                    break
            x = x + 1
            if x == 10:
                break
            y = 0
    print(d1)

    boardS = ""
    cntCheckx = 0
    while cntCheckx < 10:
        cntChecky = 0
        while cntChecky < 10:
            boardS += (d1[(cntCheckx,cntChecky)])
            cntChecky = cntChecky + 1
        boardS += "\n"
        cntCheckx = cntCheckx + 1
    print(boardS)



    cntx = 0
    while cntx < 10:
        cnty = 0
        while cnty < 10:
            if (d1[(cntx,cnty)] == "B" and not inShips(cntx, cnty)) :
                shipType = ShipType.shipType("B")
                if(d1[(cntx+1,cnty)] == "B"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif(d1[(cntx,cnty+1)] == "B"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "C" and not inShips(cntx, cnty)) :
                shipType = ShipType.shipType("C")
                if(d1[(cntx+1,cnty)] == "C"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (d1[(cntx, cnty + 1)] == "C"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "D" and not inShips(cntx, cnty)) :
                if (d1[(cntx + 1, cnty)] == "D"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (d1[(cntx, cnty + 1)] == "D"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "R" and not inShips(cntx, cnty)) :
                if (d1[(cntx + 1, cnty)] == "R"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (d1[(cntx, cnty + 1)] == "R"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "S" and not inShips(cntx, cnty)) :
                if (d1[(cntx + 1, cnty)] == "S"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (d1[(cntx, cnty + 1)] == "S"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            else:
                print("No ship")
            cnty = cnty + 1
        cntx = cntx + 1

    httpd.serve_forever()


run()