# Q2: Store Product Prices with Dictionary 
 
# Create a dictionary to store product names and their prices. Display the price of a 
# product given by the user. 

products = {
    "Milk" : 5.5,
    "Bread" : 3.2,
    "Eggs": 4.0
}

product_name = input("Enter product name: ")
print("Price is: ", products.get(product_name, "Product not found"))