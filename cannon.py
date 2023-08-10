from headers import *
from buildings import *


class Cannon(Building):
    def __init__(self, x, y, gameboard, col):
        self._body = np.array([[".", "_", "_", "."], ["|", "_", "_", "|"], [
                              "_", "/", "\\", "_"]])  # 3x4 tiles
        self.color = col
        self.range = 7
        self.atk = 80
        # top left corner, hp, xrange, yrange
        Building.__init__(self, x, y, 250, 3, 4)
        for i in range(0, 3):
            for j in range(0, 4):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i, y+j, col)

    def remove(self, gameboard):
        x = self.getx()
        y = self.gety()
        # gameboard[x][y]=' '

    def shoot(self, col, gameboard, barbsalive, bkalive):
        x = self.getx()
        y = self.gety()
        for i in range(0, 3):
            for j in range(0, 4):
                gameboard.updateboard(x+i, y+j, self._body[i][j])
                gameboard.updatecolorboard(x+i, y+j, col)

        manhattandist = 30

        # for i in range(self.getx()-self.range,self.getx()+self.range+1):
        #     for j in range(self.gety()-self.range,self.gety()+self.range+1):

        for obj in barbsalive:
            x = obj.getx()
            y = obj.gety()
            x_ = self.getx()
            y_ = self.gety()
            dist = abs(x-x_)+abs(y-y_)
            if dist < manhattandist:
                manhattandist = dist
                actualobj = obj

        for obj in bkalive:
            x = obj.getx()
            y = obj.gety()
            x_ = self.getx()
            y_ = self.gety()
            dist = abs(x-x_)+abs(y-y_)
            if dist < manhattandist:
                manhattandist = dist
                actualobj = obj

        if manhattandist < 30:
            f=0
            if actualobj.getx() > self.range + self.getx() or actualobj.getx() < self.getx() - self.range or actualobj.gety() > self.range + self.gety() or actualobj.gety() < self.gety() - self.range:
                f=1
            if f==0 :
                actualobj.health = actualobj.health-self.atk
                actualobj.health = max(0, actualobj.health)
                if actualobj in barbsalive:
                    if actualobj.gethealth()/actualobj.getmaxhp() < 0.50:
                        actualobj.setcolor(4)
                
                print(actualobj.health)
                #color change

                if actualobj.health == 0:
                    ff=0
                    if actualobj in barbsalive:
                        ff=1
                        barbsalive.remove(actualobj)
                    else:
                        ff=2
                        bkalive.remove(actualobj)
                    if ff==1:
                        for i in range(actualobj.getx(), actualobj.getx()+actualobj.getxrange()):
                            for j in range(actualobj.gety(), actualobj.gety()+actualobj.getyrange()):
                                # print('ye')
                                gameboard.updateboard(i, j, ' ')
                                gameboard.updatecolorboard(i,j,0)
                    elif f==2:
                        for i in range(actualobj.getx()-1, actualobj.getx()+actualobj.getxrange()-1):
                            for j in range(actualobj.gety()-1, actualobj.gety()+actualobj.getyrange()-1):
                                # print('ye')
                                gameboard.updateboard(i, j, ' ')
                                gameboard.updatecolorboard(i,j,0)
                 
                
