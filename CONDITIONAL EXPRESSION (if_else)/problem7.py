'''Write a program to find out whether a given post is talking about “Saurabh” or not.'''

post = input("Enter the post: ")
if "Saurabh" or "saurabh" in post:
    print("The post is talking about Saurabh.")
else:
    print("The post is not talking about Saurabh.")