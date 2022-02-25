import getpass
import stdiomask

from miscUtils import *
from visualUtils import *

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
