import secrets
import bcrypt


#main user class --> requires username and password to function as intended
class User:
	def __init__(self, userName, userPassword):
		self.userName = userName
		self.userPassword = userPassword

	def query(self, item):
		possible_queries: dict = {
			"userName": self.userName,
            "userPassword": self.userPassword
        }

		return possible_queries[item]

	def login(self, target):
		for line in open(target,"r").readlines():
			login_info = line.split()
		
			for detail in login_info:
				if self.userName == login_info[login_info.index(detail)] and self.userPassword == login_info[login_info.index(detail)+1]:
					print(self.userName) 
					break
				else:
					continue

	def store(self):
		file = open("details.txt","a")
		file.write(self.userName)
		file.write(" ")
		file.write(self.userPassword)
		file.write("\n")
		file.close()


user1 = User('soma', 123)
user1.login('old_usernames_and_passwords.txt')



def main():
	prompt = int(input("Login[1] or create new user?[2] --> "))

	if prompt == 1:
		username_prompt = input("Username: ")
		password_prompt = input("Password: ")
		login(username_prompt, password_prompt)

	elif prompt == 2:
		new_username_prompt = input("New Username: ")
		new_password_prompt = input("New Password: ")
		create_new_user(new_username_prompt, new_password_prompt)

		username_prompt = input("\nUsername: ")
		password_prompt = input("Password: ")
		login(username_prompt, password_prompt)