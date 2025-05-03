# Example 5. Looping Lists: Calculating Statistics

sales = [1500, 2000, 1800, 2200, 2500]

# Loop through the list to calculate total and average sales
total_sales = 0
for sale in sales:
    total_sales += sale

average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)