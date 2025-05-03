# 6. Filtering Products Based on Price Range 
 
# A supermarket stores product prices in a list. Write a Python program to extract products that cost between $50 and $100.

# List of product prices
product_prices = [45, 78, 120, 55, 95, 34, 85, 150, 60, 99]

# Filter products in the given price range 
filtered_prices = [price for price in product_prices if 50 <= price <= 100]

# Print result 
print("Product in price range $50 - $100: ", filtered_prices)