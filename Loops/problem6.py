#Write a program to calculate the factorial of a given number using for loop.
# 5! = 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i  
print(f"Factorial of {number} is {factorial}")
# The above code calculates the factorial of a given number using a for loop.