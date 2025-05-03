# Q6: Product Inventory System 
 
# Build a mini inventory system where you can store product names as keys and their quantity as values. 

# Hint: Use a dictionary and update values when stock increases or decreases.

# Step 1: Create the inventory dictionary
inventory = {
    "Laptops": 10,
    "Headphones": 25,
    "Keyboards": 15
}

# Step 2: Increase stock
inventory["Laptops"] += 5  # restock 5 laptops

# Step 3: Decrease stock (e.g., items sold)
inventory["Headphones"] -= 3  # sold 3 headphones

# Step 4: Add a new product
inventory["Mouse"] = 20

# Step 5: Display the inventory
print("Current Inventory:\n")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")