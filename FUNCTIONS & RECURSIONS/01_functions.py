# Function to calculate the average of three numbers
def calculate_average():       #function definition
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    avg = (a + b + c) / 3
    print("Average of a, b, c is: ", avg)

calculate_average()  # Call the function to execute it
print("Function executed successfully.")  