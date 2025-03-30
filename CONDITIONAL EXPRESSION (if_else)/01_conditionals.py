a = int(input("Enter your age: "))

# Check if the age is valid and determine voting eligibility

if a >= 18:
    print("You are an adult. You can vote.")

elif a < 0:
    print("Age can not be negative!!")

elif a == 0:
    print("You are a newborn. You can not vote.")    

else:
    print("You are a minor. You can not vote.")
    
print("End of program.")    