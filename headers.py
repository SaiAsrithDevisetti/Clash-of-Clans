import time
import numpy as np
import signal
import os
import sys
from colorama import init, Fore, Back, Style
init()
import random
from getch import _getChUnix as getChar
from art import *

SCREEN=200
HEIGHT=45
WIDTH=500
def game_load():
    os.system('aplay -q ./sounds/coc_opening.wav&')
    for i in range(20):
        print()
    art_1=text2art("                                                   CLASH OF CLANS                                                              ")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+art_1)
    for i in range(10):
        print()
    print('Press any key to play.....')

def game_overwin():

    art_1=text2art("VICTORY")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+art_1)

def game_overlose():
    art_1=text2art("DEFEAT")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+art_1)

class Cursor:
    def __init__(self):
        self.__hide_string = "\x1b[?25l"
        self.__show_string = "\x1b[?25h"
    def hide(self):
        print(self.__hide_string)
    def show(self):
        print(self.__show_string)  


