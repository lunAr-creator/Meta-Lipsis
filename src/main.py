import getpass
import hashlib
import json
import os, os.path
import random
import requests
import secrets
import string
import stdiomask
import socket
import sys
import time

from time import sleep

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
    return (socket.gethostbyname(socket.gethostname()), requests.get('http://ip.42.pl/raw').text)

#Make hashes for comparisons and storing in .txt file 'accountfile.txt
def make_hash(data):
	return hashlib.sha256(str.encode(data)).hexdigest()

def check_hash(data, hash):
	if make_hash(data) == hash:
		return True

	return False


#Functions that deal with creation, authorisation and login process of the user
def get_existing_users():
    if does_exist('accountfile.txt'):
        with open('accountfile.txt', 'r') as fp:
            for line in fp.readlines():
                (username, password) = line.split()
                yield (username, password)
    else:

        f = open('accountfile.txt', 'a')
        f.close()
        get_existing_users()

def is_authorized(username, password):
    l = int(sum(map(len, get_existing_users())) / 2)
    print()

    loading_bar(0, l, prefix=' Checking Accounts:', suffix='Complete', length=l)

    time.sleep(1)
    for i in range(0, l):
        sleep((random.randint(3, 5))/10)
        loading_bar(i + 1, l, prefix=' Checking Accounts:', suffix='Complete', length=l)

    return any(check_hash(username, user[0]) and check_hash(password,
           user[1]) for user in get_existing_users())

def get_user():
	username = input("\n Username: ")
	password = stdiomask.getpass(prompt=" Password: ")

	return username, password

def make_user():
	if len(list(get_existing_users())) == 4:
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
		with open("accountfile.txt","a") as file:
			file.write(make_hash(new_username))
			file.write(" ")
			file.write(make_hash(new_password))
			file.write("\n")

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
			time.sleep(1)
			print(f"\n Welcome back {username}")
			# reminder_exit()

		else:
			time.sleep(1)
			print("\n Incorrect login details, or physical key not present")
			# reminder_exit()


#Main menu loop!!!
def main():
	menu_art(1)
	screen_line()
	ips = get_ip()
	print(f" Type 'Help' to get started")

	while True:
		choice = get_input(f'\n mainMenu@{socket.gethostname()[8:len(socket.gethostname())]}\n → ', 
			[["Docu", "Returns the documentation for this program"], ["Login", "Login to a pre-existing account"], ['New User', 'Create a new user - found in "accountfile.txt" '], ["Ip", "Returns host computers private ip"], ["Cls", "Clear the main menu"], ["Exit", "Exit the program - will give 3s warning"]])


		if choice == "Login":
			authorisation()
			break

		elif choice == "New User":
			make_user()
			break

		elif choice == "Ip":
			print(f"\n Public_IP: {ips[1]}, Private_IP: {ips[0]}")

		elif choice == "Docu":
			documentation()

		elif choice == "Cls":
			cls()

		elif choice == "Exit":
			reminder_exit()
			break

main()


