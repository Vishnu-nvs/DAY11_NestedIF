USER_NAME="Python"
Password="Django"
user_name=input("Please Enter the Username:")
password=input("Please Enter the Password:")
if USER_NAME== user_name:
    if Password == password:
        print("Succesfully login")
    else:
        print("Invalid password")
else:
    print("User is not exist")
