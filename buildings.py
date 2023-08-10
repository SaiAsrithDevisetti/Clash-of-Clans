from headers import *


class Building():
    #top left corner, hp, xrange, yrange
    def __init__(self, x, y, hp, x_, y_):
        self._xcoord = x
        self._ycoord = y
        self.health = hp
        self.maxhp = hp
        self.xrange = x_
        self.yrange = y_

    def getx(self):
        return self._xcoord

    def setx(self, x):
        self._xcoord = x

    def gety(self):
        return self._ycoord

    def sety(self, y):
        self._ycoord = y
    
    def gethp(self):
        return self.health
    
    def sethp(self, x):
        self.health = x
    
    def setmaxhp(self,x):
        self.maxhp = x
    
    def getmaxhp(self):
        return self.maxhp
    
    def getxrange(self):
        return self.xrange

    def setxrange(self, x):
        self.xrange = x
    
    def getyrange(self):
        return self.yrange

    def setyrange(self, x):
        self.yrange = y
