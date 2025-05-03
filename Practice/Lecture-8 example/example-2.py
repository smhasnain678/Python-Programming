# Example 2. Changing List Items: Normalizing Data

price_dollars = [100, 200, 300, 400]

conversion_rate = 270 # 1 USD = 270 PKR

# Changing list items to convert prices to pkr
prices_pkr = [price * conversion_rate for price in price_dollars]

print("Prices in PKR:", prices_pkr)