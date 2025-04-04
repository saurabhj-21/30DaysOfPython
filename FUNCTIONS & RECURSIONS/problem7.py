#Write a python function to remove a given word from a list ad strip it at the same time.

lst = ["apple", "banana", "cherry", "date"]
word_to_remove = " banana "
print("Original list:", lst)

def remove_word_and_strip(lst, word_to_remove):
    # Strip the word and remove it from the list if it exists
    stripped_word = word_to_remove.strip()
    if stripped_word in lst:
        lst.remove(stripped_word)
    return lst

print("Word to remove:", word_to_remove.strip())
lst = remove_word_and_strip(lst, word_to_remove)
print("Updated list:", lst)