# Taking customer review as input
review = input("Enter the customer review: ").lower()

# Checking if the word "bad" is NOT present
if "bad" not in review:
    print("\nThe review is positive or neutral.")
else:
    print("\nThe review might be negative.")
