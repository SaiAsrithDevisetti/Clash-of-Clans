from headers import *
from buildings import *

#500 hp

class TownHall(Building):
    def __init__(self, x, y, gameboard, col):
        self._body = np.array([[".","_","."],["/"," ","\\"],["|"," ","|"],["|","_","|"]]) # 4x3 tiles
        self.color = col
        Building.__init__(self, x, y, 600, 4, 3)
        for i in range(0,4):
            for j in range(0,3):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i,y+j,col)
    
    def remove(self, gameboard):
        x = self.getx()
        y = self.gety()
        # gameboard[x][y]=' '
