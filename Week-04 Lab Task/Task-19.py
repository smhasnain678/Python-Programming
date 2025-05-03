# Q7: Countries in Asia and Commonwealth 
 
# You have two lists: one of Asian countries and one of Commonwealth countries. Find 
# countries that are in both groups. 

# Hint: Use set intersection to solve this. 

# List of Asian countries
asian_countries = ["Pakistan", "India", "Bangladesh", "China", "Malaysia", "Singapore"]

# List of Commonwealth countries
commonwealth_countries = ["India", "Pakistan", "Australia", "Canada", "Bangladesh", "UK"]

# Convert both lists to sets
asian_set = set(asian_countries)
commonwealth_set = set(commonwealth_countries)

# Use set intersection to find common countries
common_countries = asian_set.intersection(commonwealth_set)

# Display result
print("Countries in both Asian and Commonwealth groups:")
for country in common_countries:
    print(country)
