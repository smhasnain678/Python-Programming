# Taking product description and keyword as input
product_description = input("Enter the product description: ").lower()
keyword = input("Enter the keyword to search: ").lower()

# Checking if the keyword is present in the description
if keyword in product_description:
    print("\nKeyword found in the description!")
else:
    print("\nKeyword not found in the description.")
