# Question: 
# Write a program that counts how many times each word appears in a given sentence using a dictionary.

sentence = "data science is fun and data is powerful"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    
print("Word Count:", word_count)