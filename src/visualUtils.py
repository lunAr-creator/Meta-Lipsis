import time
import sys
import itertools
import random

from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

def moving_ellipsis(content):
    print(content, end="")

    time.sleep(0.5)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(1)

    print("\n")

def print_text(text: str, sleep_time: float = 0.0) -> None:
    """
    Prints the text to the console character by character. RPG style.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)
    if sleep_time != 0.0:
        time.sleep(sleep_time)

def spinner(time):
    spinner = itertools.cycle([' -', '/', '|', '\\', ' '])
    c = 0
    while c < time:
        sys.stdout.write(next(spinner))
        sleep(0.3)   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')
        c += 1

        if c == time:
            break

def loading_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} [{bar}] {percent}% {suffix}', end='\r')

    if iteration == total:
        print()

def menu_art(selection):
    if selection == 1:
        print(r"""
                    _______ _______ _______ _______             _____  _____  _______ _____ _______
                    |  |  | |______    |    |_____|      |        |   |_____] |______   |   |______
                    |  |  | |______    |    |     |      |_____ __|__ |       ______| __|__ ______|
        """)
        print()

def screen_line():
    print(f' ____<2022v2.4.3-alpha>_______________________________________________________________________________________________')