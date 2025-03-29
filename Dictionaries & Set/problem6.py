'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
'''

# Create an empty dictionary
friends_languages = {}
# Allow 4 friends to enter their favorite language
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
friends_languages.update({name: language})

#for fiend two
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
friends_languages.update({name: language})

#for friend three
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
friends_languages.update({name: language})

#for friend four
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
friends_languages.update({name: language})

print(friends_languages) # Display the dictionary