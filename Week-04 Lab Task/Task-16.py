# Q4: Daily Temperatures 
 
# You record temperatures for a week in degrees Celsius. How will you store this data if 
# you want it to be unchangeable? 

# Hint: Use a tuple to store the daily temperature values.

# Weekly temperatures in Celsius (unchangeable)
temperatures = (22.5, 24.0, 21.8, 23.2, 25.1, 26.3, 24.7)

# Display the temperatures
print("Weekly Temperatures (°C):")
for i, temp in enumerate(temperatures, start=1):
    print(f"Day {i}: {temp}°C")
