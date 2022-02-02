import time
import sys
import itertools, sys
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



def menu_art(selection):
    if selection == 1:
        print(r"""
                /|    //| |             v0.05                / /                                        
               //|   // | |     ___    __  ___  ___         / /        ( )  ___      ___     ( )  ___    
              // |  //  | |   //___) )  / /   //   ) )     / /        / / //   ) ) ((   ) ) / / ((   ) ) 
             //  | //   | |  //        / /   //   / /     / /        / / //___/ /   \ \    / /   \ \     
            //   |//    | | ((____    / /   ((___( (     / /____/ / / / //       //   ) ) / / //   ) )   
        """)
               
def line_by_line():
    time.sleep(0.05)
    print(r"""                   /|    //| |             v0.05                / /                                        """)
    time.sleep(0.05)
    print(r"""                  //|   // | |     ___    __  ___  ___         / /        ( )  ___      ___     ( )  ___    """)
    time.sleep(0.05)
    print(r"""                 // |  //  | |   //___) )  / /   //   ) )     / /        / / //   ) )  ((   ) ) / / ((   ) ) """)
    time.sleep(0.05)
    print(r"""                //  | //   | |  //        / /   //   / /     / /        / / //___/ /    \ \    / /   \ \     """)
    time.sleep(0.05)
    print(r"""               //   |//    | | ((____    / /   ((___( (     / /____/ / / / //       //   ) ) / / //   ) )   """)


def screen_line():
    print(' _____________________________________________________________________________________________________________________')


		
