from headers import *
from spell import *


class Heal(Spell):
    #top left corner, hp, xrange, yrange
    def __init__(self, heal):
        Spell.__init__(self,0,0,heal)

    def affecttroops(self,barbsalive,bkalive,gameboard):
        for obj in barbsalive:
            obj.sethealth(min(obj.gethealth()+(self.getheal()*5/100)*obj.gethealth(), obj.getmaxhp()))
            if obj.gethealth()/obj.getmaxhp() >= 0.5:
                obj.setcolor(2)
        for obj in bkalive:
            obj.sethealth(min(obj.gethealth()+(self.getheal()/100)*obj.gethealth(), obj.getmaxhp()))
