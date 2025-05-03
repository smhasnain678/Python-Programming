# Q9: Dictionary of Country-Capital Pairs 
 
# Create a program to store countries and their capitals. Ask the user for a country and return its capital.

capitals = {"Malaysia": "Kuala Lumper", "Pakistan": "Islamabad", "Japan": "Tokyo"}

country = input("Enter a country :")

print("Capitals :", capitals.get(country, "Country not found"))