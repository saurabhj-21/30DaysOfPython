'''Write a program to find whether a given username 
contains less than 10 characters or not.'''

username = input("Enter your username: ")
if len(username) < 10:
    print("Username is less than 10 characters.")
elif len(username) == 10:
    print("Username is exactly 10 characters.")
else:
    print("Username is greater than or equal to 10 characters.")