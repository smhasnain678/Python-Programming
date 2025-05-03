# Q20: Real Estate Listings Filter 
 
# A real estate agency has a list of property prices. Write a program to filter the properties that 
# fall within a specific price range and sort these filtered prices in ascending order. 

# Hint: 
# Use a list comprehension to filter the list based on the price range, then apply the sort() 
# method to the filtered list.

# Sample list of property prices
property_prices = [500000, 120000, 750000, 300000, 450000, 650000, 350000]

# Define the price range
min_price = 300000
max_price = 600000

# Step 1: Filter the list based on the price range using list comprehension
filtered_prices = [price for price in property_prices if min_price <= price <= max_price]

# Step 2: Sort the filtered list in ascending order
filtered_prices.sort()

# Display the sorted filtered prices
print("Filtered and Sorted Property Prices:", filtered_prices)
