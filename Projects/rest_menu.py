# Define the menu of restaurant
menu = {
    "Pizza": 450,
    "Pasta": 230,
    "Chicken Burger": 180,
    "Roll": 220,
    "Coffee": 80,
    "Sandwish": 350,
    "Deserts": 250
}

# Greet 
print("Welcome to restaurant")
print("Pizza: Rs450/=\nPasta: Rs230/=\nChicken Burger: Rs180/=\nRoll: Rs220/=\nCoffee: Rs80/=\nSandwish: Rs350/=\nDeserts: Rs250/=")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] 
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")
        
print(f"The total amount of item to pay is {order_total}")