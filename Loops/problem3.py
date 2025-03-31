#Write a program to print multiplication table of a given number using while loop.

i = int(input("Enter a number: "))

j = 1
while(j<=10):
    print(f"{i} x {j} = {i*j}")
    j+=1