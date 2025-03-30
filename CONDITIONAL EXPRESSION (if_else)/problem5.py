#Write a program which finds out whether a given name is present in a list or not.

name = ("John", "Alice", "Bob", "Charlie", "David")
get_name = input("Enter a name: ")

if get_name in name:
    print(f"{get_name} is present in the list.")
else:
    print(f"{get_name} is not present in the list.")

print("Names in the list are: ", name)
# The code takes a name as input and checks if it is present in the predefined list of names.