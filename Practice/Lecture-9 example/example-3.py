# Example.3 
# COunting the frequency of unique categories in a Dataset

from collections import Counter

# Transaction types in an e-commerce dataset
transactions = ("Refund", "Purchase", "Purchase", "Refund", "Subscription", "Purchase", "Subscription", "Purchase")

# CountNo of Occurreneces of each item using Counter
transaction_counts = Counter(transactions)

# Display transaction frequency
print(transaction_counts)