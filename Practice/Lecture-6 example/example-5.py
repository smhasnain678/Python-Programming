# Sample review
review = "This product is absolutely Amazing! "

# Step 1: Conver to lowercase
review = review.lower()

# Step 2: Trim Spaces
review = review.strip()

# Step 3: Split the text int words
words = review.split()

# Step 4: Define positive and negative words
positive_words = ["Amazing", "excellent", "great", "good", "love"]
negative_words = ["bad", "worst", "horrible", "disappointed", "poor"]

# Step 5: Check Sentiments
sentiment = "Neutral" 
for word in words:
    if word in positive_words:
        sentiment = "Positive"
        break
    elif word in negative_words:
        sentiment = "Negative"
        break

print("Processed Review:", review)
print("Sentiments Analysis Result:", sentiment)

        