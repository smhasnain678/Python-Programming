original_price = float(input("Enter the original price of the product: "))
discount_percent = float(input("Enter the discount percentage: "))
discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount
print("Final price after discount:", final_price)