
# HTTPRequestHandler class
class Ship:

    def __new__(self, startX, startY, endX, endY, length, name):
        self.location = (startX, startY, endX, endY)
        self.name = str(name);
        return
    def hit(self, x, y):
        return True
