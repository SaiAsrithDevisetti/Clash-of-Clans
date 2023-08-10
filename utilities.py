import os
import json
from colorama import Fore, Back
import sys
import termios
import tty
import signal
from time import sleep
from re import sub
from random import choice

from headers import *
from board import *

gboard = Board(HEIGHT, WIDTH)
gboard.create_game_board()


class Input:

    def _get_key_raw(self):
        fd = sys.stdin.fileno()
        self.old_config = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.buffer.raw.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, self.old_config)
        return ch

    def _timeout_handler(self, signum, frame):
        raise TimeoutError

    def get_parsed_input(self, timeout=0.1):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            ip = self._get_key_raw()
            signal.alarm(0)
            if ip == b'\x03':
                key = 'quit'
            elif ip in [b'a', b'A']:
                key = 'bkleft'
            elif ip in [b'd', b'D']:
                key = 'bkright'
            elif ip in [b's', b'S']:
                key = 'bkdown'
            elif ip in [b'w', b'W']:
                key = 'bkup'
            elif ip == b' ':
                key = 'space'
            elif ip == b'\r':
                key = 'enter'
            # elif ip in [b's', b'S']:
            #     key = 'skip'
            elif ip in [b'1']:
                key = 'spawn1'
            elif ip in [b'2']:
                key = 'spawn2'
            elif ip in [b'3']:
                key = 'spawn3'
            elif ip in [b'4']:
                key = 'spawnbk1'
            elif ip in [b'5']:
                key = 'spawnbk2'
            elif ip in [b'6']:
                key = 'spawnbk3'
            elif ip in [b'7']:
                key = 'heal'
            elif ip in [b'8']:
                key = 'rage'
            elif ip in [b'9']:
                key = 'AOE'
            else:
                key = 'none'
            sleep(timeout)
            return key
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None
