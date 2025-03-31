'''Write a program to print the following star pattern.
* * *
*   * 
* * * 
for n = 3
'''

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() # The above code prints a star pattern with the number of rows specified by the user.
# The above code prints a star pattern with the number of rows specified by the user.