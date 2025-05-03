# Q13: Product Inventory Updates 
 
# A store maintains a list of product quantities. When new shipments arrive, you need to update 
# the list by appending new quantities and removing items that are out of stock. 

# Hint: 
# Use list methods such as append(), extend(), and remove() to update your inventory list. 

product_quantities = [25, 5, 0, 15, 8, 0, 20, 12, 22, 10]

new_shipments = [12, 7, 9,]

# Add new shipments to inventory using extend()
product_quantities.extend(new_shipments)

# Remove out-of-stock items (i.e., quantity 0)
# remove() only removes one occurrence at a time
while 0 in product_quantities:
    product_quantities.remove(0)
        
print("Updated Inventory:", product_quantities)