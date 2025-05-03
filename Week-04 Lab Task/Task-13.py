# Q13: Find Common Customers 

# You have two customer lists from two branches of a store. Find customers who visited both branches. 

# Hint: Use set intersection to find common elements between two customer sets.

branch_a = {"Ali", "Sara", "Usman", "Fatima", "Ahmed", "Zainab"}

branch_b = {"Zainab", "Ahmed", "Hassan", "Iqra", "Sara", "Bilal"}

common_customer = branch_a.intersection(branch_b)

print("These Customers visited both branches", common_customer)
