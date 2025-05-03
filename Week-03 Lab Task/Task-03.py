#3. Filter Out Students Who Scored Above 80% 
 
# A university conducted an exam, and student scores are stored in a list. Write a Python 
# program to extract and display only the students who scored above 80%.

# List of student scores
scores = [78, 85, 92, 65, 88, 73, 95, 80, 79, 90]

# Filter students who scored above 80
high_scorers =  [score for score in scores if score > 80] 

print("Final Score: ", high_scorers)