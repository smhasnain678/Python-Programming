# Taking full name as input
full_name = input("Enter your full name: ")

# Calculating length (excluding spaces)
name_length = len(full_name.replace(" ", ""))

# Displaying the result
print(f"\nTotal number of characters (excluding spaces): {name_length}")
