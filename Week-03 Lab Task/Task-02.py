# 2. Analyze Monthly Sales Data

# A store records its daily sales for a month (30 days). Write a program to: 
# • Find the total and average sales. 
# • Identify the highest and lowest sales day.

# List of daily sales (in USD) 
sales = [200, 340, 550, 450, 615, 760, 240, 810, 120, 770, 620, 460, 510, 220, 590, 720, 360, 800, 600, 420, 270, 230, 180, 410, 750, 490, 440, 530, 640, 315]

# Compute total, average, max, and min sales 
total_sales = sum(sales)
average_sales = total_sales / len(sales)
max_sales = max(sales)
min_sales = min(sales)

# Print results 
print("Total Sales: ", total_sales, "USD")
print("Average Daily Sales: ", round(average_sales, 2), "USD")
print("Highest Sales: ", max_sales, "USD")
print("Lowest Sales: ", min_sales, "USD")