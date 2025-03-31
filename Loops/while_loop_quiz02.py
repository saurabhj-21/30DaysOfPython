# Now, write a program to print 1 to 50 using a while loop but skip the numbers that are divisible by 5 and 3.
i = 1
while(i <= 50):
    if i % 5 != 0 and i % 3 != 0:
        print(i)
    i = i + 1
