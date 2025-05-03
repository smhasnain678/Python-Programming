# Q4: Tuple for Geolocation Coordinates 
 
# Create a list of tuples representing coordinates (latitude, longitude) of tourist attractions. 

locations = [
    ("KL Tower", (3.1528, 101.7037)),
    ("Petronas Towers", (3.1579, 101.7113)), 
    ("Batu Caves", (3.2379, 101.6841))
]

for place, coords in locations:
    print(place, "is located at", coords)