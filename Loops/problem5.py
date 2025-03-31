#Write a program to find the sum of first n natural numbers using while loop.

limit = int(input("Enter boundary: "))
sum = 0
i = 1  
while(i <= limit):
    sum += i
    i += 1
print(f"Sum of first {limit} natural numbers is {sum}")
# The above code calculates the sum of the first n natural numbers using a while loop.