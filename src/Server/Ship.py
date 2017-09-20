from enum import Enum

class ShipOrientation(Enum):
    HorizontalRight = 0
    HorizontalLeft = 1
    VerticalUp = 2
    VerticalDown = 3

class ShipType(Enum):
    Carrier = ("C", 5)
    Battleship = ("B", 4)
    Cruiser = ("R", 3)
    Submarine = ("S", 3)
    Destroyer = ("D", 1)

    @classmethod
    def has_value(cls, value):
        return (any(value == item.value[0] for item in cls))
    @classmethod
    def shipType(cls, value):
        for item in cls:
            print(value[0])
            if(value == item.value[0]):
                return item
        return None

class Ship:
    # Initializes all properties
    def __new__(self, startX, startY, endX, endY, shipType):
        self.location = (startX, startY, endX, endY)
        self.shipType = shipType
        self.length = shipType.value[1]
        self.hits = 0

        self.orientation = ShipOrientation.HorizontalLeft

        if(startX == endX):
            if(startX > endX):
                self.orientation = ShipOrientation.HorizontalLeft
            else:
                self.orientation = ShipOrientation.HorizontalRight
        else:
            if(startY > endY):
                self.orientation = ShipOrientation.VerticalDown
            else :
                self.orientation = ShipOrientation.VerticalUp
        print(self.orientation.name)
        return self

    def __contains__(self, item, hit):
        x = int(item[0])
        y = int(item[1])

        print(str(x) + " " + str(y))

        if(True or self.orientation == ShipOrientation.VerticalUp):
            if((x == self.location[0]) and (y >= self.location[1]) and (y <= (self.location[1] + self.length-1))):
                print("hits " + str(self.hits))
                if hit:
                    self.hits = self.hits + 1
                print("hits " + str(self.hits))
                return True
            else: return False
        elif (self.orientation == ShipOrientation.VerticalDown):
            if (x == self.location[0] and y >= (self.location[1] - self.length+1) and y <= self.location[1]):
                print("hits " + str(self.hits))
                if hit:
                    self.hits = self.hits + 1
                print("hits " + str(self.hits))
                return True
            else:
                return False
        elif (self.orientation == ShipOrientation.HorizontalRight):
            if ( y == self.location[0] and x >= self.location[1] and x <= (self.location[1] + self.length-1)):
                    print("hits " + str(self.hits))
                    if hit:
                        self.hits = self.hits + 1
                    print("hits " + str(self.hits))
                    return True
            else:
                    return False
        else:
            if (y == self.location[0] and x >= (self.location[1] - self.length + 1) and x <= self.location[1]):
                print("hits " + str(self.hits))
                if hit:
                    self.hits = self.hits + 1
                print("hits " + str(self.hits))
                return True
            else:
                return False
    def sunk(self):
        print(str(self.hits))
        return self.hits == 2*self.length

    def validate(self):
        # if(self.location[0] != self.location[2] and self.location[1] != self.location[3]):
        #     print("Invalid " + self.shipType.name + ". Ship can not be diagonal\n")
        #     return False
        if (self.orientation == ShipOrientation.HorizontalRight or self.orientation == ShipOrientation.HorizontalLeft and abs(self.location[0] - self.location[2]) != self.shipType.value[1]):
            print("Invalid " + self.shipType.name + ". Ship has length " + abs(self.location[0] - self.location[2]) + " but should have length" + self.shipType[1] +" \n")
            return False
        else:
            return True

