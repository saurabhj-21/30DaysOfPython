#Write a recursive function to calculate the sum of first n natural numbers.

limit = int(input("Enter the limit: "))
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)
sum = sum_of_natural_numbers(limit)
print(f"The sum of first {limit} natural numbers is {sum}.")