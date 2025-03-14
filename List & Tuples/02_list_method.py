friends=["apple", "orange", 5, 345.06, False, "akash", "rohan"]
print(friends)

friends.append("Saurabh") #Add new thing in a list
print(friends)

friends.insert(3, 222)    #will add 222 at index 3
print(friends)

#sorting the value
l1=[1,23, 42, 5, 67, 91]  #MIN to MAX
l1.sort()
print(l1)

l2=[1,3, 2, 5, 7, 9]      #MAX to MIN
l2.reverse()
print(l2)

l3=[2, 5, 6, 1, 90, 23]
l3.pop(2)                 #Will delete element at index 2 and return its value.
print(l3)

l4=[5, 2, 4, 7, 1, 9]
l4.remove(5)              #Will remove 21 from the list.
print(l4)

#take unsorted input on this list from user and print the inputs sorted
l5 = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sorting the list
l5.sort()
# Printing the sorted list
print("Sorted list:", l5)

#Reversly sorted
l3.reverse()
print("Reversely sorted list:", l5)
