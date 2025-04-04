# Write a program using functions to find greatest of three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def gratest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the greatest number.")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the greatest number.")
        return num2
    else:
        print(f"{num3} is the greatest number.")
        return num3
gratest_number(num1, num2, num3)