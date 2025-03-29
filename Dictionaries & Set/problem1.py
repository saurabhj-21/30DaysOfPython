'''Write a program to create a dictionary
of Bengali words with values as their English 
translation. Provide user with an option to look it up!'''


words = {"আমি": "I", "তুমি": "You", "সে": "He/She", "আমরা": "We", "তুমি": "You", "তারা": "They"}

Your_word = input("Enter the Bengali word you want to translate: ") 
print(words.get(Your_word, "Word not found!"))