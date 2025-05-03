# 1. Calculate Average Daily Temperature 

# A weather station records daily temperatures for a week. Write a Python 
# program to store the temperatures in a list and calculate the average temperature for the week.

# List of temperatures recorded each day (in Celsius)
temperatures = [30.5, 32.0, 31.2, 29.8, 28.5, 33.1, 30.0]

# Calculate average temperature 
average_temperature = sum(temperatures) / len(temperatures)

# Print the result 
print("Average Weekly Temperature:", round(average_temperature, 2), "°C")