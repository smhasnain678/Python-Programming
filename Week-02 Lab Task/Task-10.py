# Taking sentence input
sentence = input("Enter a sentence: ")
word_to_check = input("Enter a word to check: ")
# Checking if the word is not in the sentence
not_found = word_to_check not in sentence
# Displaying result
print("\nWord Not Found:", not_found)