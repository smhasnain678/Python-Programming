from collections import Counter
# 5. Most Frequent Customer Orders 
 
# A restaurant keeps track of 10 customers' orders in a list. Write a program to find the most 
# frequently ordered item. 

# List of customer orders
orders =  ["Burger", "Pizza", "Pasta", "Pizza", "Burger", "Burger", "Salad", "Pizza", "Pasta", "Burger"] 

# Count occurrences of each item
order_counts = Counter(orders)

# Find the most ordered item
most_ordered = order_counts.most_common(1)[0]

# Print Result
print("Most Order Item: ", most_ordered[0], "(", most_ordered[1], "times)")