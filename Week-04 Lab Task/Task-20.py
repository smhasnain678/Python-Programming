# Q8: Store Student Grades 
 
# Store the names of students along with a list of their scores in three subjects. Then calculate their average. 

# Hint: Use a dictionary where each key is a student name, and the value is a list or tuple of scores.


# Step 1: Create the student grade dictionary
students = {
    "Ali": [85, 78, 92],
    "Sara": [90, 88, 95],
    "Usman": [70, 75, 80],
    "Fatima": [88, 79, 85]
}

# Step 2: Calculate and display average for each student
print("Student Averages:\n")
for name, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"{name}: Average = {average:.2f}")
