# Taking user input
name = input("Enter customer name: ")
age = input("Enter customer age: ")
phone = input("Enter customer phone number: ")

# Converting age to integer
age = int(age)

# Displaying customer details with their data types
print("\nCustomer Details:")
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Phone Number: {phone} (Type: {type(phone)})")
