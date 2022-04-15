import os

from visualUtils import *

class Main:
	def __init__(self, account_file="accountfile.txt"):
		self.account_file = account_file

	def visual_initialise(self, startup_funcs: list):
		for command in startup_funcs: 
			yield command

	def get_existing_users(self):
	    if os.path.isfile(self.account_file):

	        with open(self.account_file, 'r') as fp:
	            for line in fp.readlines():
	                (username, password) = line.split()
	                yield (username, password)

	    else:
	        f = open(self.account_file, 'a')
	        f.close()
	        self.get_existing_users()

	def run_func(self, func):
		return func

	def get_help(self, given_list):
		print("\n Help:")
		lens = []
		
		for i in range(len(given_list)):
			for j in range(len(given_list[i])):
				lens.append(len(given_list[i][0]))

		for i in range(len(given_list)):
			output2 = []

			for j in range(len(given_list[i])):
				output = f"{given_list[i][j]}"
				output2.append(output)

			calc = ((max(lens)+min(lens))-len(given_list[i][0]))
			dots = '.'*calc
			info = f'{dots}: '.join(output2)

			print(f"   {info}") 

	def get_input(self, string: str, valid_options: list) -> str:
	    while True:
	        user_input = input(string)
	        if user_input == '':
	        	continue
	        else:
		        capitalized = user_input[0].upper() + user_input[1:len(user_input)]

	        options = []
	        for i in range(len(valid_options)):

	            for j in range(len(valid_options[i])):
	                option = f'{valid_options[i][j-1]}'
	            options.append(option)

	        if user_input in options or capitalized in options:
	            return capitalized

	        elif capitalized == 'Help':
	        	return self.get_help(valid_options)

	        print(f" -Please select from: {', '.join(options)} or Help-")


main = Main()

main.visual_initialise([menu_art(1), screen_line(), print(" Type 'Help' to get started")])

options = [
			["Docu", "Returns the documentation for this program"],
			["Login", "Login to a pre-existing account"],
			['New User', 'Create a new user - found in "accountfile.txt" '], 
			["Ip", "Returns host computers private ip"], 
			["Cls", "Clear the main menu"], 
			["Exit", "Exit the program - will give 3s warning"]
		  ]

main.get_input(f'\n mainMenu@{socket.gethostname()[8:len(socket.gethostname())]}\n → ', options)

