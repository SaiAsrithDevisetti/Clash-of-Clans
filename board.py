from headers import *
import colorama
from colorama import Fore


# color codes followed
#0 -> no color (white)
#1 -> Green color
#2 -> Yellow color
#3 -> Red color  


class Board:
    def __init__(self, rows, cols):
        self.__rows__ = rows
        self.__cols__ = cols
        self.spawningpoint1 = [5,10]
        self.spawningpoint2 = [20,50]
        self.spawningpoint3 = [35,150]
        self.gameboard = []
        self.colorboard = []              # color of each cell

    # Creating a plain screen

    def create_game_board(self):
        for i in range(self.__rows__):
            self.arr = []
            for j in range(self.__cols__):
                self.arr.append(" ")
            self.gameboard.append(self.arr)
        for i in range(self.__rows__):
            self.arr = []
            for j in range(self.__cols__):
                self.arr.append(0)
            self.colorboard.append(self.arr)

    def displayboard(self, offset):
        for i in range (self.__rows__):
            for j in range (offset, SCREEN + offset):
                if self.colorboard[i][j]==0:
                    print(Fore.RESET + self.gameboard[i][j], end='')
                elif self.colorboard[i][j]==1:
                    print(Fore.GREEN + self.gameboard[i][j], end='')
                elif self.colorboard[i][j]==2:
                    print(Fore.YELLOW + self.gameboard[i][j], end='')
                elif self.colorboard[i][j]==3:
                    print(Fore.RED + self.gameboard[i][j], end='')   
                elif self.colorboard[i][j]==4:
                    print(Fore.YELLOW + Style.DIM + self.gameboard[i][j] + Style.RESET_ALL, end='') 
            print(" ", end='\n')
    
    def updateboard(self,x,y,c):
        self.gameboard[x][y]=c
    
    def updatecolorboard(self,x,y,col):
        self.colorboard[x][y]=col
    
    def vacant(self,x,y):
        if self.gameboard[x][y]==' ':
            return True
        else:
            return False
    
    def getcell(self,x,y):
        return self.gameboard[x][y]
