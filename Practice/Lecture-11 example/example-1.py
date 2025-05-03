# Customer Information Stored in Dictionary
customer_data = {
    "Customer_ID": 101,
    "Name": "Alice Jhonson",
    "Age": 30,
    "Email": "alice@example.com",
    "ُPurchaseHistory": ["Laptop", "Smartphone", "Headphones"]
}

# Accessing Specific Details
customer_name = customer_data["Name"]
customer_email = customer_data.get("Email") # Using get() to safely access values

# Display customer information
print("Customer Name:", customer_name)
print("Customer Email:", customer_email)