import bcrypt
#store your password:
password = str(input("input password: ")) 
# Encode the stored password:
password = password.encode('utf-8')
# Encrypt the stored pasword:
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
# Create an authenticating password input field to check if a user enters the correct password: 
check = str(input("check password: ")) 
# Encode the authenticating password as well:
check = check.encode('utf-8') 
# Use conditions to compare the authenticating password with the stored one:
if bcrypt.checkpw(check, hashed):
 print("login success")
else:
 print("incorrect password")