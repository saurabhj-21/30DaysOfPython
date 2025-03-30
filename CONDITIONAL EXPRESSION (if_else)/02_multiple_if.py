a = int(input("Enter your age: "))

#if statement number 1
if a%2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")
    
# if statement number 2

if a >= 18:
    print("You are an adult. You can vote.")

elif a < 0:
    print("Age can not be negative!!")

elif a == 0:
    print("You are a newborn. You can not vote.")    

else:
    print("You are a minor. You can not vote.")
    
print("End of program.")    