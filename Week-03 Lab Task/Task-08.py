# 8. Count Occurrences of Words in a List 
 
# A blogger wants to analyze which words are used frequently in their articles. Write a program that counts the occurrences of words in a list. 

from collections import Counter 

word = ["data", "analytics", "python", "data", "AI", "analytics", "python", "data", "data", "ML"]

# Count word occurrences 
word_count = Counter(word)

# Print Result
print("Word Frequency: ", word_count)