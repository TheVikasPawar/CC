# Import
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Passing json file to cred object for credential and initializing the same
cred = credentials.Certificate("Vikas.json")
firebase_admin.initialize_app(cred)

# taking user input for authenticating
email = input("Email :")
password = input("Password :")

# Pushing email and password on authentication and printing success message
user = auth.create_user(email = email , password = password)
print("success".format(user.email))
