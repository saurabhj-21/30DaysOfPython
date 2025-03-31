#Write a program to find whether a given number is prime or not.

number = int(input("Enter a number: "))

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")
# The above code checks if a given number is prime or not using a for loop.