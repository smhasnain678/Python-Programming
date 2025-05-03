# Q15: Course Registration List Update 
 
# A course has an existing list of registered students. New registrations need to be added, and 
# then the list should be sliced to create a sublist for a special workshop invitation (e.g., the first 
# 10 names). 

# Hint: 
# Use append() to add new names and list slicing to extract the first 10 entries. 

registered_students = ["Ali", "Sara", "John", "Mehak", "David", "Ayesha"]

new_students = ["Bilal", "Zara", "Usman", "Nida", "Faisal", "Tina"]

# Add each new student using a loop and append()
for student in new_students:
    registered_students.append(student)

# Slice the first 10 names for the workshop
workshop_invitees = registered_students[:10]

print("Workshop Invitees:", workshop_invitees)
