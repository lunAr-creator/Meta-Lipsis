import socket
import secrets
import requests
import hashlib
import os

from visualUtils import *

#Miscellaneous Functions
def reminder_exit():
	moving_ellipsis("\n Exiting program")

def get_help(given_list):
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

def get_input(string: str, valid_options: list) -> str:
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
        	return get_help(valid_options)

        print(f" -Please select from: {', '.join(options)} or Help-")

def generate_token(size=15):
    return secrets.token_urlsafe(size)[:size]

def is_command(command_given):
	return command_given.startswith('/', 0, 1)

def does_exist(file_name):
	return os.path.isfile(file_name)

def get_ip():
    return (socket.gethostbyname(socket.gethostname()), requests.get("https://www.wikipedia.org").headers["X-Client-IP"])

#Make hashes for comparisons and storing in .txt file 'accountfile.txt
def make_hash(data):
	return hashlib.sha256(str.encode(data)).hexdigest()

def check_hash(data, hash):
	if make_hash(data) == hash:
		return True

	return False