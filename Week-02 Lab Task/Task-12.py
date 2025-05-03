# Taking user input for meal price
meal_price = float(input("Enter the meal price: "))

# Calculating total bill with 6% tax
tax = meal_price * 0.06
total_bill = meal_price + tax

# Displaying the results
print("\nBill Details:")
print(f"Meal Price: ${meal_price:.2f}")
print(f"Sales Tax (6%): ${tax}")
print(f"Total Bill: ${total_bill:.2f}")
