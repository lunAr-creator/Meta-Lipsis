import time
import sys

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


def menu_art(selection):
	if selection == 1:
		print("""  
		 ___   _      ___   _      ___   _      ___   _      ___   _
	 	[(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
	  	 '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
	        /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /
	     	  |____________|____________|____________|____________|
	                             |            |            |
	                         ___  \_      ___  \_      ___  \_
	                        [(_)] |=|    [(_)] |=|    [(_)] |=|
	                         '-`  |_|     '-`  |_|     '-`  |_|
	                        /mmm/        /mmm/        /mmm/

	    """)

	elif selection == 2:
		print(r"""
    /|    //| |             v0.05                / /                                        
   //|   // | |     ___    __  ___  ___         / /        ( )  ___      ___     ( )  ___    
  // |  //  | |   //___) )  / /   //   ) )     / /        / / //   ) ) ((   ) ) / / ((   ) ) 
 //  | //   | |  //        / /   //   / /     / /        / / //___/ /   \ \    / /   \ \     
//   |//    | | ((____    / /   ((___( (     / /____/ / / / //       //   ) ) / / //   ) )   
""")


		
