#Write a program to find the greatest of four numbers entered by the user.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

if(number1>=number2 and number1>=number3 and number1>=number4):
    print("The greatest number is: ", number1)
elif(number2>=number1 and number2>=number3 and number2>=number4):
    print("The greatest number is: ", number2)
elif(number3>=number1 and number3>=number2 and number3>=number4):
    print("The greatest number is: ", number3)
else:
    print("The greatest number is: ", number4)
# The above code is a simple program that takes four numbers as input from the user and determines the greatest of the four numbers using conditional statements. It uses a series of if-elif-else statements to compare the numbers and print the greatest one. The program is straightforward and easy to understand, making it suitable for beginners learning about conditional statements in Python.