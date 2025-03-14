d=(3, 22, 3, 66, True, "Rocky", 3, "Vai")
print(d)

#count()
no=d.count(3)
print(no)      #Counts the events of occuring 3 in the tuple

#index()
t = (10, 20, 30, 20, 40)
print(t.index(20))  # Output: 1 (first occurrence of 20)
print(len(t))       # Returns the total number of elements in the tuple.

#tuple() (Type conversion function)
list = [1, 2, 3]
con_to_tuple = tuple(list)   #Converts an iterable (like a list) into a tuple.
print(con_to_tuple)  

'''Since tuples are immutable, 
they do not have methods like 
append(), remove(), or sort() (which lists have).'''


#Some operations

#Concatenation
t1=(1, 3, 4, 5)
t2=(22, 44, 11, 55)
result=t1+t2
print(result)

# Repetation
t3=(3, 4, 5)
result3=t3*3
print(result3)

# Slicing
t4=(2, 5, 6, 7, 9)
print(t4[1:3])
print(t4[:4])
print(t4[-2:])

# Membership (Checking if an element exists in a tuple)
t5=(3, 6, 7, 8, 4)
print(7 in t5)
print(11 in t5)
print(10 not in t5)

# Iteration
t6 = ("apple", "banana", "cherry")
for item in t6:
    print(item)

# Tuple Unpacking (Assigning tuple values to variables.)
t7 = (10, 20, 30)
a, b, c = t7
print(a, b, c)