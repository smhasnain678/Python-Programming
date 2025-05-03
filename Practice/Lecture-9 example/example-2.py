# Example. 2 
# Detecting COmmon Customers Between Two Data Sources (Using Sets)

# Customer IDs from Platform A
platform_a_customer = {101, 102, 103, 104, 105}

# Customer IDs from Platform B
platform_b_customer = {104, 105, 106, 107, 108}

# Find Common customers who purchased from both platforms
common_customers = platform_a_customer & platform_b_customer # Intersection operation

# Display COmmon Customer
print(common_customers)

