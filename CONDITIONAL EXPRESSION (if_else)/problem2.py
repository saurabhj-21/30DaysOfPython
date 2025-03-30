'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''

subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))

# Calculate total marks and percentage
total_marks = subject1 + subject2 + subject3
percentage = (total_marks) / 300  # Assuming each subject is out of 100

if percentage >= 0.4 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    print("You have passed the exam.", "Your percentage is:", percentage * 100, "%")
else:
    print(f"You have failed the exam with {percentage * 100} %. Try again Next year!")
