import getpass
import hashlib
import random
import secrets
import string
import stdiomask
import socket
import os, os.path
import sys
import time

from time import sleep
from visualUtils import moving_ellipsis, print_text, menu_art, spinner, \
    screen_line, loading_bar

#Miscellaneous Functions
def reminder_exit():
	moving_ellipsis("\n Exiting program")

def get_help(given_list):
    print(" Help: \n -----------------------")
    
    for i in range(len(given_list)):
        output2 = []

        for j in range(len(given_list[i])):
            output = f"{given_list[i][j]}"
            output2.append(output)

        print(f" {': '.join(output2)}")

    print(" -----------------------")

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

        elif capitalized == 'Exit':
            reminder_exit()
            return False

        elif capitalized == 'Help':
        	return get_help(valid_options)

        print(f" -Please select from: {' or '.join(options)} and Help-")

def generate_token(size=15):
    return secrets.token_urlsafe(size)[:size]

def is_command(command_given):
	return command_given.startswith('/', 0, 1)

def does_exit(file_name):
	return os.path.isfile(file_name)


#Make hashes for comparisons and storing in .txt file 'accountfile.txt
def make_hash(data):
	return hashlib.sha256(str.encode(data)).hexdigest()

def check_hash(data, hash):
	if make_hash(data) == hash:
		return True

	return False


#Functions that deal with creation, authorisation and login process of the user
def get_existing_users():
    if does_exit('accountfile.txt'):
        with open('accountfile.txt', 'r') as fp:
            for line in fp.readlines():
                (username, password) = line.split()
                yield (username, password)
    else:

        f = open('accountfile.txt', 'a')
        f.close()
        get_existing_users()

def is_authorized(username, password):
    l1 = len(list(get_existing_users()))
    l2 = sum(map(len, get_existing_users()))
    print()

    loading_bar(0, l1, prefix=' Checking Usernames:', suffix='Complete', length=l1)

    for i in range(0, l1):
        sleep(0.3)
        loading_bar(i + 1, l1, prefix=' Checking Usernames:', suffix='Complete', length=l1)

    loading_bar(0, l2, prefix=' Checking Validity:', suffix='Complete', length=l2)

    for i in range(0, l2):
        sleep(0.3)
        loading_bar(i + 1, l2, prefix=' Checking Validity:', suffix='Complete', length=l2)

    return any(check_hash(username, user[0]) and check_hash(password,
           user[1]) for user in get_existing_users())

def get_user():
	username = input("\n Username: ")
	password = stdiomask.getpass(prompt=" Password: ")

	return username, password

def make_user():
	if len(list(get_existing_users())) == 3:
		print(" The number of available accounts [3] has been reached.\n If you wish to create more, simply modify the account file.")

		moving_ellipsis("\n Redirecting to login process")
		authorisation()

	else:
		new_username = input("\n New Username: ")
		while True:
			new_password = input(" New Password: ")
			confirm = stdiomask.getpass(prompt=" Confirm Password: ")

			if confirm == new_password:
				moving_ellipsis("\n > Your Passwords Match. Continuing process")
				break

			else:
				print("\n > Passwords do not match. Try again")

		#hash usernames and passwords before writing to .txt file
		file = open("accountfile.txt","a")
		file.write(make_hash(new_username))
		file.write(" ")
		file.write(make_hash(new_password))
		file.write("\n")
		file.close()

		if is_authorized(new_username, new_password):
			try:
				moving_ellipsis("\n Redirecting to login process")
				authorisation()
			except Exception as e:
				print(f" Fail encountered during sub-process {make_user.__name__}. Error: {e}")
		else:
			print(" Something went wrong. Try again later :D")

		return False

def authorisation():
	if len(list(get_existing_users())) == 0:
		print(" No exisiting users in account file")

		moving_ellipsis("\n Redirecting to user creation process")
		make_user()

	else:
		username, password = get_user()

		if is_authorized(username, password):
			# spinner(5)
			print(f"\n Welcome back {username}")
			reminder_exit()

		else:
			print("\n Incorrect login details")
			reminder_exit()


#Main menu loop!!!
def main():
	menu_art(1)
	screen_line()
	print(" Type 'Help' to get started")

	while True:
		choice = get_input(f'\n mainMenu@{socket.gethostname()}~{sys.platform}\n → ', 
			[["Login", "Login??"], ['New User', 'Create new user']])


		if choice == "Login":
			authorisation()
			break

		elif choice == "New User":
			make_user()
			break

		elif choice == False:
			break

main()


