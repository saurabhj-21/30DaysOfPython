marks = {
    "Swapnil": 100,
    "Saurabh": 56,
    "John": 75,
    2 : "Jane"
}
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Swapnil"))

marks.update({"Saurabh" : 60, 2 : "Rihanna", "Robin" : 88, }) # Update the value of the key "Saurabh"
print(marks)

# Remove a key-value pair using pop
marks.pop("John")
print(marks)

# Remove and return an arbitrary key-value pair using popitem
removed_item = marks.popitem()
print(f"Removed item: {removed_item}")
print(marks)

# Clear all items from the dictionary
marks.clear()
print(marks)