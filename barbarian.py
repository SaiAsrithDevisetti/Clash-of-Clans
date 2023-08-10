from headers import *
from troop import *

class Barbarian(Troops):
    def __init__(self,x,y,gameboard,col):
        self._body = 'B'
        self.color = col
        Troops.__init__(self,x,y,25,1,1,100)
        gameboard.updateboard(x,y,self._body)
        gameboard.updatecolorboard(x,y,col)
    
    def remove(self,gameboard):
        x=self.getx()
        y=self.gety()
        # gameboard[x][y]=' '
    
    def move(self,x,y,oldx,oldy,gameboard):
        gameboard.updateboard(oldx,oldy,' ')
        gameboard.updateboard(x,y,'B')
        self.setx(x)
        self.sety(y)
        gameboard.updatecolorboard(oldx,oldy,0)
        gameboard.updatecolorboard(x,y,self.color)
        return
    
    def checkcollisionright(self,gameboard):
        x=self.getx()
        y=self.gety()
        if y >= 199:
            return False
        elif gameboard.vacant(x,y+1)==False:
            return False
        else:
            return True
    
    def checkcollisionleft(self,gameboard):
        x=self.getx()
        y=self.gety()
        if y <= 0:
            return False
        elif gameboard.vacant(x,y-1)==False:
            return False
        else:
            return True
    
    def checkcollisionup(self,gameboard):
        x=self.getx()
        y=self.gety()
        if x <= 0:
            return False
        elif gameboard.vacant(x-1,y)==False:
            return False
        else:
            return True
    
    def checkcollisiondown(self,gameboard):
        x=self.getx()
        y=self.gety()
        if x >= 44:
            return False
        elif gameboard.vacant(x+1,y)==False:
            return False
        else:
            return True
    
    def setcolor(self,col):
        self.color=col