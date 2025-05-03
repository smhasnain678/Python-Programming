# Q14: Unique Event Attendees 
 
# A list of event attendees (names) contains duplicates. Write a program to remove duplicate 
# names and then sort the unique names alphabetically. 
 
# Hint:
# Consider converting the list to a set to eliminate duplicates, then back to a list and sort it. 

# List with duplicate attendee names
attendees = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]

# Remove duplicates by converting to a set, then back to a list
unique_attendees = list(set(attendees))

# Sort alphabetically
unique_attendees.sort()

print("Unique Attendees (Alphabetically):", unique_attendees)


