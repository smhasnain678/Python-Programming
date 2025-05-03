# Q19: Library Book Collection Management 
 
# A library has a list of book titles, but some titles appear more than once. Remove duplicates 
# from the list and add a few new arrivals at the beginning of the list. 

# Hint: 
# Convert the list to a set to remove duplicates, then convert it back to a list. Use the insert() 
# method to add new titles at the beginning.

# Sample list of book titles
books = ["The Great Gatsby", "1984", "Moby Dick", "1984", "To Kill a Mockingbird", "Moby Dick"]

# Step 1: Remove duplicates by converting the list to a set, then back to a list
unique_books = list(set(books))

# Step 2: Add new arrivals at the beginning of the list using insert()
new_arrivals = ["The Catcher in the Rye", "Pride and Prejudice"]
for book in new_arrivals:
    unique_books.insert(0, book)

# Display the updated list of books
print("Updated Book List:", unique_books)
