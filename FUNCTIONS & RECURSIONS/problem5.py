'''Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def print_pattern(n):
    for i in range(n, 0, -1): # Loop from n to 1 (inclusive)
        # Print '*' i times
        print('*' * i)

# Test the function
n = int(input("Enter the number of lines: "))
print_pattern(n)