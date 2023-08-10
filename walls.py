from headers import *
from buildings import *


# 200 hp

class Walls(Building):
    def __init__(self, x, y, gameboard, type, col):
        if type == 0:
            self._body = '|'
        else:
            self._body = '_'
        self.color = col
        Building.__init__(self, x, y, 200, 1, 1)
        gameboard.updateboard(x, y, self._body)
        gameboard.updatecolorboard(x,y,col)

    def remove(self, gameboard):
        x = self.getx()
        y = self.gety()
        # gameboard[x][y]=' '
