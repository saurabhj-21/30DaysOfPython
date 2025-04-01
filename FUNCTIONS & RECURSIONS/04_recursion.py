'''
factorial(0) = 1
factorial(1) = 1 
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 5 x 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x factorial(n-1)

'''
# This code calculates the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is {factorial(n)}.")