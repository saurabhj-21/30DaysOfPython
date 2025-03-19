# Program to accept marks of 6 students and display them in a sorted manner

# Accept marks of 6 students
marks = []
for i in range(6):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

# Sort the marks
marks.sort()

# Display the sorted marks
print("Sorted marks:", marks)