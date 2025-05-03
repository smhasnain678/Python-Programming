# Example 4. Removing List Items: Cleaning Data

ages = [25, -1, 30, -5, 40, 22, -10]

# Removing invalid ages (negative values)
cleaned_ages = [age for age in ages if age >= 0]

print("Cleaned ages ", cleaned_ages)