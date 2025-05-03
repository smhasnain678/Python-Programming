# Q5: Word Frequency in Article 
 
# Count how many times each word appears in a short news article. 

# Hint: Split the string into words and use a dictionary to count occurrences using word: frequency. 

# Sample article text
article = "Pakistan's tech industry is growing fast. Tech startups are booming in Pakistan."

# Split the string into words
words = article.split()

# Create an empty dictionary for word frequencies
word_freq = {}

# Count each word's frequency
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display the result
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
