import secrets
import string
import random
import hashlib
import getpass
import stdiomask

from visualUtils import moving_ellipsis, print_text, menu_art, spinner, screen_line
from misc import get_input, get_help

def make_hash(data):
	return hashlib.sha256(str.encode(data)).hexdigest()

def check_hash(data, hash):
	if make_hash(data) == hash:
		return True

	return False

#generates token for securely connecting to server
def generate_token(size=15):
    return secrets.token_urlsafe(size)[:size]

def get_existing_users():
    with open("accountfile.txt", "r") as fp:
         for line in fp.readlines():
             username, password = line.split()
             yield username, password

def is_authorized(username, password):
    # return any((user == (username, password) for user in get_existing_users()))
    return any((check_hash(username, user[0])) and check_hash(password, user[1]) for user in get_existing_users())

def get_user():
	username = input("\n Username: ")
	password = stdiomask.getpass(prompt=" Password: ")

	return username, password

def make_user():
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
	username, password = get_user()

	if is_authorized(username, password):
		print(f"\n Welcome back {username}")
	elif not is_authorized(username, password):
		print("\n Incorrect login details")

def main():
	menu_art(2)
	screen_line()
	help_line = '		Type Login or New User'
	print(help_line.rjust(int(118/2)), " ")

	while True:
		choice = get_input('\n meta lipsis ~v0.05 \n → ', ["Login", "New User", "Help"])

		if choice == "Login":
			authorisation()
			break

		elif choice == "New User":
			make_user()
			break

		elif choice == "Help":
			get_help([["Login", "Login??"], ['New User', 'Create new user']])

if __name__ == '__main__':
	main()