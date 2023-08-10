from headers import *
from troop import *


class King(Troops):
    def __init__(self, x, y, gameboard, col):
        self._body = np.array([["o", " "], ["|", "/"], ["/", "\\"]])
        self.color = col
        # position of sword, atk pnts of bk, xrange, yrange, hp
        Troops.__init__(self, x+1, y+1, 80, 3, 2, 300)
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i, y+j, col)

    def remove(self, gameboard):
        x = self.getx()
        y = self.gety()
        x = x-1
        y = y-1
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x+i, y+j, ' ')
                gameboard.updatecolorboard(x+i, y+j, 0)

    def move_forward(self, gameboard):
        x = self.getx()
        y = self.gety()
        x = x-1
        y = y-1

        y = y+1  # forward
        self.remove(gameboard)
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i, y+j, self.color)

        self.setx(x+1)
        self.sety(y+1)

    def move_backward(self, gameboard):
        x = self.getx()
        y = self.gety()
        x = x-1
        y = y-1

        y = y-1  # backward
        self.remove(gameboard)
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i, y+j, self.color)

        self.setx(x+1)
        self.sety(y+1)

    def move_up(self, gameboard):
        x = self.getx()
        y = self.gety()
        x_ = x-1
        y_ = y-1
        x_ = x_-1  # up
        self.remove(gameboard)
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x_+i, y_+j, self._body[i][j])
                gameboard.updatecolorboard(x_+i, y_+j, self.color)

        self.setx(x_+1)
        self.sety(y_+1)

    def move_down(self, gameboard):
        x = self.getx()
        y = self.gety()
        x_ = x-1
        y_ = y-1

        x_ = x_+1  # down
        self.remove(gameboard)
        for i in range(0, 3):
            for j in range(0, 2):
                gameboard.updateboard(x_+i, y_+j, self._body[i][j])
                gameboard.updatecolorboard(x_+i, y_+j, self.color)

        self.setx(x_+1)
        self.sety(y_+1)

# King
# o
# |/ {x,y}   right wrt sword by one cell
# /\

    def checkcollisionright(self, gameboard):
        x = self.getx()
        y = self.gety()
        if y >= 199:
            return False
        elif gameboard.vacant(x-1, y+1) == False or gameboard.vacant(x, y+1) == False or gameboard.vacant(x+1, y+1) == False:
            return False
        else:
            return True

    def checkcollisionleft(self, gameboard):
        x = self.getx()
        y = self.gety()
        if y <= 1:
            return False
        elif gameboard.vacant(x, y-2) == False or gameboard.vacant(x+1, y-2) == False or gameboard.vacant(x-1, y-2) == False:
            return False
        else:
            return True

    def checkcollisionup(self, gameboard):
        x = self.getx()
        y = self.gety()
        if x <= 2:
            return False
        elif gameboard.vacant(x-2, y) == False or gameboard.vacant(x-2, y-1) == False:
            return False
        else:
            return True

    def checkcollisiondown(self, gameboard):
        x = self.getx()
        y = self.gety()
        if x >= 43:
            return False
        elif gameboard.vacant(x+2, y) == False or gameboard.vacant(x+2, y-1) == False:
            return False
        else:
            return True
