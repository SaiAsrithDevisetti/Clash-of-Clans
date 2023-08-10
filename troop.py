from headers import *


class Troops():

    # position, atk points, xrange, yrange
    def __init__(self, x, y, atk, x_, y_, hp):
        self._xcoord = x
        self._ycoord = y
        self.atk = atk
        self.xrange = x_
        self.yrange = y_
        self.health = hp
        self.maxhp = hp

    def getx(self):
        return self._xcoord

    def setx(self, x):
        self._xcoord = x

    def gety(self):
        return self._ycoord

    def sety(self, y):
        self._ycoord = y

    def getatk(self):
        return self.atk

    def setatk(self, x):
        self.atk = x

    def getxrange(self):
        return self.xrange

    def setxrange(self, x):
        self.xrange = x
    
    def getyrange(self):
        return self.yrange

    def setyrange(self, y):
        self.yrange = y
    
    def gethealth(self):
        return self.health
    
    def sethealth(self, x):
        self.health = x
    
    def getmaxhp(self):
        return self.maxhp
    
    def setmaxhp(self, x):
        self.maxhp = x
