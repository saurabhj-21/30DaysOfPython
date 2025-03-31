#Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
# The above code prints the multiplication table of a given number in reversed order using a for loop.