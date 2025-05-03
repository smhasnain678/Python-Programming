# Q14: Store Employee Records 
 
# You want to store employee data including name, age, and department for each 
# employee. How will you organize this data?

# Hint: Use a dictionary where the key is the employee name and the value is a tuple with (age, department). 

employee_data = {
    "Ali" : (28, "Finance"),
    "Sara" : (25, "HR"),
    "Zain" : (27, "IT"),
    "Usman" : (25, "Marketing"),
}

print("Employee Records:\n")

for name, (age, department) in employee_data.items():
    print(f"Name: {name}, Age: {age}, Department: {department} ")