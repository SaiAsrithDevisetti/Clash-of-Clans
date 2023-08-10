from headers import *


class Spell():
    #top left corner, hp, xrange, yrange
    def __init__(self, damage, spid, inchealth):
        self.dam = damage
        self.speed = spid
        self.heal = inchealth

    def getdamage(self):
        return self.dam

    def setdamage(self, x):
        self.dam = x

    def getspeed(self):
        return self.speed

    def setspeed(self, y):
        self.speed = y
    
    def getheal(self):
        return self.heal
    
    def setheal(self, x):
        self.heal = x
