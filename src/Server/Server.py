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

        x = query[0][1]
        y = query[1][1]

        print('query: ' + str(x) + str(y))

        if( not str(x).isdigit() or not str(y).isdigit()):
            #HTTP Bad Request
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return

        x = int(query[0][1])
        y = int(query[1][1])

        if (x > 9 or x < 0 or y > 9 or y < 0):
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return

        if( d1[(x,y)] == "X" or d1[(x,y)] == "H"):
            #HTTP Gone
            self.send_response(410)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return




        inShips(x,y, True)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("hit=" + status + "&sunk=" + str(sunk), "utf8"))
        return
def inShips(x, y, hit):
    global status
    global sunk
    for ship in Ships:
        if ( ship.__contains__(ship, (x, y), hit)):
            status = "1"
            sunk = ship.shipType.value[1] if ship.sunk(ship) else "0"
        else:
            status = "0"
            sunk = 0
    return
def resetShips():
    print('Resetting ships')
    for ship in Ships:
        ship.hits = 0
        print(ship.shipType.name)
    return
def run():
    print('starting Battleship...')

    global status
    global sunk
    global Ships
    Ships = []

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


    global d1
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
            if (d1[(cntx,cnty)] == "B" and not inShips(cntx, cnty, False)) :
                shipType = ShipType.shipType("B")
                if(cntx < 9 and d1[(cntx+1,cnty)] == "B"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif(cnty < 9 and d1[(cntx,cnty+1)] == "B"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (cnty < 9 and d1[(cntx,cnty)] == "C" and not inShips(cntx, cnty, False)) :
                shipType = ShipType.shipType("C")
                if(cntx < 9 and d1[(cntx+1,cnty)] == "C"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (cnty < 9 and d1[(cntx, cnty + 1)] == "C"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "D" and not inShips(cntx, cnty, False)) :
                shipType = ShipType.shipType("D")
                if (cntx < 9 and d1[(cntx + 1, cnty)] == "D"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (cnty < 9 and d1[(cntx, cnty + 1)] == "D"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "R" and not inShips(cntx, cnty, False)) :
                shipType = ShipType.shipType("R")
                if (cntx < 9 and d1[(cntx + 1, cnty)] == "R"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (cnty < 9 and d1[(cntx, cnty + 1)] == "R"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            elif (d1[(cntx,cnty)] == "S" and not inShips(cntx, cnty, False)) :
                shipType = ShipType.shipType("S")
                if (cntx < 9 and d1[(cntx + 1, cnty)] == "S"):
                    Ships.append(Ship(cntx, cnty, cntx + shipType.value[1], cnty, shipType))
                elif (cnty < 9 and d1[(cntx, cnty + 1)] == "S"):
                    Ships.append(Ship(cntx, cnty, cntx, cnty + shipType.value[1], shipType))
            cnty = cnty + 1
        cntx = cntx + 1

    for ship in Ships:
        print("fuck" + str(ship.shipType))

    # resetShips()

    httpd.serve_forever()


run()