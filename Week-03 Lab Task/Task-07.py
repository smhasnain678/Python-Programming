# 7. Extracting Even and Odd Numbers 
 
# A sports coach wants to divide players into two teams based on their jersey numbers. Write a program that separates even and odd jersey numbers.

# List of player jersey numbers 
jersey_numbers = [12, 7, 18, 9, 25, 6, 14, 21, 4, 11]

# Separate even and odd numbers 
even_numbers = [num for num in jersey_numbers if num % 2 == 0]
odd_numbers = [num for num in jersey_numbers if num % 2 != 0]

# Print Result
print("Team A (Even Jersey): ", even_numbers)
print("Team A (Odd Jersey): ", odd_numbers)