# Q11: Employee Performance Rankings 
 
# Q: A company has a list of employee performance scores. Write a program to sort these scores
# and extract the top 5 performers. 

#Hint: Use the list’s sort method (or sorted function) and then slice the list to get the top elements. 

employee_scores = [120, 130, 90, 170, 80, 75, 85, 100, 50, 150, 60]

# Sort in descending order
sorted_scores = sorted(employee_scores, reverse=True)

# Get top 5
top_five = sorted_scores[:5]

print(top_five)