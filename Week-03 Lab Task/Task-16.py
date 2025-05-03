# Q16: Daily Expense Tracker 
 
# A budget tracker maintains a list of daily expenses. If a day's expense is missing, insert it in 
# the correct chronological position and then compute the total expense for the week. 

# Hint: 
#Use the insert() method to add a missing expense and sum() to calculate the total.

daily_expenses = [120, 150, 100, 0, 180, 130]  # Assume index 3 (Thursday) is missing

daily_expenses.insert(3, 140)

thissum = sum(daily_expenses)

print(thissum)