# Taking two complex impedance values as input
z1 = complex(input("Enter first impedance (in a+bj format): "))
z2 = complex(input("Enter second impedance (in a+bj format): "))

# Performing addition and multiplication
z_sum = z1 + z2
z_product = z1 * z2

# Displaying the results
print("\nResultant Impedance:")
print(f"Sum: {z_sum}")
print(f"Product: {z_product}")
