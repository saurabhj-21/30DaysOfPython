# Create an empty list to store numbers
numbers = []

# Input 8 numbers from user
print("Please enter 8 numbers:")
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Convert list to set to get unique numbers, then back to list
unique_numbers = list(set(numbers))

# Display unique numbers
print("Unique numbers are:", unique_numbers)