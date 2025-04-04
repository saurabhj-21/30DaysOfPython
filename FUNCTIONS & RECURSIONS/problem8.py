#Write a python function to print multiplication table of a given number.

input_number = int(input("Enter a number: "))
def multiplication_table(number):
    for i in range(1, 11): # Loop from 1 to 10 (inclusive)
        print(f"{number} x {i} = {number * i}") # Print the multiplication result
multiplication_table(input_number) # Call the function with the input number
# The function takes a number as input and prints its multiplication table from 1 to 10.