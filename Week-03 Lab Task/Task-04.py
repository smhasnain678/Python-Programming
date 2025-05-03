# 4. Stock Price Analysis 
 
# A financial analyst records the closing stock prices of a company over 10 days. Write a program to: 
# • Find the highest and lowest stock prices. 
# • Calculate the average stock price.

# List of stock prices over 10 days
stock_prices = [102.5, 101.8, 105.3, 107.2, 98.6, 103.4, 106.9, 99.3, 100.5, 108.1]

# Compute highest, lowest, and average prices
max_price = max(stock_prices)
min_prices = min(stock_prices)
avg_prices = sum(stock_prices) / len(stock_prices)

# Print Result 
print("Highest Stock Price:", max_price, "USD") 
print("Lowest Stock Price:", min_prices, "USD") 
print("Average Stock Price:", round(avg_prices, 2), "USD") 
