#Write a program to detect double space in a string.

#Using find()
text=input("Enter your text: ")

#chech if double spaces exist
position=text.find(" ")
if position != -1:
    print(f"Double space found at index {position}")
else:
    print("Double space doesn't exist!")

#Replace the double space from problem with single space.
update_text=text.replace("  ", " ")
print(update_text)