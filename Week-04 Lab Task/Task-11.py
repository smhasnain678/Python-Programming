# Q11. Remove Duplicates from a List of Strings Using a Set 

# Write a Python program to remove all duplicates from a given list of strings and return a 
# list of unique strings. Use the Python set data type.


# Define a function 'remove_duplicates' that takes a list of 'strings' as input. 
def remove_duplicates(strings): 
# Convert the 'strings' list into a set to remove duplicate elements. 
 return list(set(strings)) 

# Define a list of strings 'strs' for testing. 
strs = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz'] 
print("Original list of strings:") 
print(strs) 

# Call the 'remove_duplicates' function and print the list of unique strings. 
print("List of strings after removing duplicates:") 
print(remove_duplicates(strs)) 

# Repeat the process for a different input list. 
strs = ["Python", "Exercises", "Practice", "Solution", "Exercises"] 
print("\nOriginal list of strings:") 
print(strs) 

# Call the 'remove_duplicates' function and print the list of unique strings. 
print("List of strings after removing duplicates:") 
print(remove_duplicates(strs)) 