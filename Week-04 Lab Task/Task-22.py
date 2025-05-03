# Q10: Monthly Expenses Tracker 
 
# Track your monthly expenses where each item (like rent, groceries, transport) is stored along with the amount spent. 

# Hint: Use a dictionary where the key is the expense category, and the value is the amount.

# Step 1: Create a dictionary of monthly expenses
expenses = {
    "Rent": 25000,
    "Groceries": 8000,
    "Transport": 3000,
    "Utilities": 2000,
    "Internet": 1500
}

# Step 2: Calculate total monthly expenses
total = sum(expenses.values())

# Step 3: Display all expenses and total
print("Monthly Expenses:\n")
for category, amount in expenses.items():
    print(f"{category}: Rs. {amount}")

print(f"\nTotal Monthly Expenses: Rs. {total}")
