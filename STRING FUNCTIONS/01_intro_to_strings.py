name="Saurabh"
#calculate the lenth of strings
print(len(name))
print(name.startswith("sa")) #gives 'False' result(name starts with uppercase)
print(name.endswith("bh"))

#Changing Case
name2="saurabh"
print(name2.capitalize())

name3="hello saurabh"
print(name3.capitalize()) #capitalize only the first letter
print(name3.upper())      #All in upppercase
print(name3.title())      #Each fisrt letters of words are capitalize
print(name3.lower()) 

name4="SauRabh"
print(name4.swapcase())   #it swaps the cases

# Includes 'start' but excludes 'end'
print(name[-5:-1])  
print(name[2:6])

print(name[:3])
print(name[3:])


nameshort=name[0:5] #start from the index 0 to 5
print(nameshort)
character1=name[1]
print(character1)

#Checking String Properties
text = "Hello123"
print(text.isalpha())  # False (because it contains numbers)
print(text.isdigit())  # False
print(text.isalnum())  # True
print("   ".isspace()) # True

#Finding and Replacing
text = "hello world, hello universe"
print(text.find("world"))   # Returns the index of the first occurrence of a substring
print(text.index("universe"))  # raises an error if not found
print(text.count("hello"))  # Counts occurrences of a substring
print(text.replace("hello", "hi"))  # hReplaces occurrences of a substring with another string

#Splitting and Joining
text = "apple,banana,grape"
words = text.split(",")  
print(words)  # Splits a string into a list based on a separator

sentence = " ".join(words)
print(sentence)  # Joins elements of an iterable (list, tuple) into a string

#Stripping Whitespace
text = "   hello world   "
print(text.strip())   # Removes leading and trailing space
print(text.lstrip())  # Removes leading spaces
print(text.rstrip())  # Removes trailing spaces

#String Formatting
my_name = "Saurabh"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) #Formats strings with placeholders
print(f"My name is {my_name} and I am {age} years old.")  # A modern way to format strings in Python

#Reversing a String
text_01 = "Python"
print(text_01[::-1])  
