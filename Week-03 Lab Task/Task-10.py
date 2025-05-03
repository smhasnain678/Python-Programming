# Q12: Customer Order History Management 
 
# A customer’s order history is stored as a list of product names. Update this list by removing 
# any canceled orders and count how many times each product appears. 

# Hint: 
# Utilize methods like remove() to delete an order, and consider using list methods like 
# count() (or explore collections for frequency counts).

# Method. 1

from collections import Counter
customer_orders_history = ["Laptop", "Mouse", "Speakers", "Keyboard", "Hard Disk", "Headphones", "USB", "Table", "Mouse", "USB", "Laptop"]

# Canceled orders
canceled_orders = ["Mouse", "USB"]

# Remove all canceled orders
updated_list = [item for item in customer_orders_history if item not in canceled_orders]

products_count = Counter(updated_list)

print("Updated Order List: ", updated_list)
print("Product Frequency: ", products_count)


# Method. 2

customer_orders_history = [
    "Laptop", "Mouse", "Speakers", "Keyboard", 
    "Hard Disk", "Headphones", "USB", "Table", 
    "Mouse", "USB", "Laptop"  # added duplicates for counting
]

# Remove canceled orders one by one (if present)
if "Mouse" in customer_orders_history:
    customer_orders_history.remove("Mouse")  # removes first occurrence

if "USB" in customer_orders_history:
    customer_orders_history.remove("USB")  # removes first occurrence

# Count how many times each product appears using count()
for product in set(customer_orders_history):
    print(f"{product}: {customer_orders_history.count(product)}")


