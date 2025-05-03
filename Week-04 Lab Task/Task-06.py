# Q6: Inventory System using Dictionary 
 
# Simulate an inventory system where you can update and check the stock of each item. 

inventory = {"Apples": 30, "Bananas": 50, "Milk": 20}

item = input("Enter item name :" )

if item in inventory:
    print("Available", inventory[item], "units")
else:
    print("Item not found")