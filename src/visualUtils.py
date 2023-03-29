import time
import sys
import itertools
import random
import os
import socket
import requests
from time import sleep

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

def spinner(start=" Checking accounts: ", end="Finished"):
    cycle = ['-', '/', '|', '\\', ' ']
    spinner = itertools.cycle(cycle)
    c = 0
    sys.stdout.write(start)
    while c < len(cycle):
        sys.stdout.write(next(spinner))
        sleep(0.3)   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')
        c += 1
    sys.stdout.write(end)
    print("\n")

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
                                   _      _                    ______                              
                         _      __(_)____(_)____   _________  / __/ /__      ______  ________      
                        | | /| / / / ___/ / ___/  / ___/ __ \/ /_/ __/ | /| / / __ `/ ___/ _ \     
                        | |/ |/ / / /  / (__  )  (__  ) /_/ / __/ /_ | |/ |/ / /_/ / /  /  __/     
                        |__/|__/_/_/  /_/____/  /____/\____/_/  \__/ |__/|__/\__,_/_/   \___/ 
        """)
        print()

def screen_line():
    print(f' __________________________________________<Type "Help" to get started!>______________________________________________')                                                  
