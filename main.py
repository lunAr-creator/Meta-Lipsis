import secrets
import bcrypt

#generates token for user class
def generate_token(size=15):
    return secrets.token_urlsafe(size)[:size]

#main user class --> requires, username, password and token to function as intended
class User:
	def __init__(self, userName, userPassword, userToken=generate_token()):
		self.userName = userName
		self.userPassword = userPassword
		self.UserToken = userToken

	def query(self, item):
		possible_queries: dict = {
			"userName": self.userName,
            "userPassword": self.userPassword,
            "userToken": self.UserToken,
        }

		return possible_queries[item]

#create new user process
def create_new_user(new_username, new_password):
	rand_token = generate_token()
	print(rand_token)
	new_user = User(new_username, new_password, rand_token)

#main login function --> migrate to database in future (online or app generated) 
def login(username, password):

	for line in open("accountfile.txt","r").readlines(): # Read the lines
		login_info = line.split() # Split on the space, and store the results in a list of two strings
		for items in login_info:
			if username == login_info[login_info.index(items)] and password == login_info[login_info.index(items)+1]:
				user_check = User(login_info[login_info.index(items)], login_info[login_info.index(items)+1])
				break
			else:
				continue

		print(login_info)
    
	if username == user_check.query('userName') and password == user_check.query('userPassword'):
		print("Logged in")

	else:
		if username != user_check.query('userName') and password == user_check.query('userPassword'):
			print(f"Incorrect login details: Supplied username: {username}, is incorrect")

		elif username == user_check.query('userName') and password != user_check.query('userPassword'):
			print(f"Incorrect login details: Supplied password: {password}, is incorrect")

		else:
			print(f"Incorrect login details: Supplied username and password: {username}, {password} are incorrect")



#main starting function connecting all relevant functions and classes --> occurs before main func *2
def mainBefore():
	prompt = int(input("Login[1] or create new user?[2] --> "))

	if prompt == 1:
		username_prompt = input("Username: ")
		password_prompt = input("Password: ")
		login(username_prompt, password_prompt)

	elif prompt == 2:
		new_username_prompt = input("New Username: ")
		new_password_prompt = input("New Password: ")

		file = open("accountfile.txt","a")
		file.write(new_username_prompt)
		file.write(" ")
		file.write(new_password_prompt)
		file.write("\n")
		file.close()

		create_new_user(new_username_prompt, new_password_prompt)

		username_prompt = input("\nUsername: ")
		password_prompt = input("Password: ")
		login(username_prompt, password_prompt)

mainBefore()


