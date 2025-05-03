# Question: 
# Write a Python program that takes input from the user and identifies its data type. 
#  Taking input from the user 
# user_input = input("Enter any value: ")
#  Identifying the data type 
# print("\nYou entered: ", user_input)
# print("\nData Type: ", type(user_input))


# Question: 
# Write a Python program that takes a temperature in Celsius and converts it into Fahrenheit using explicit casting. 
# # Taking input as string and casting to float 
# celsius = float(input("Enter temperature in Celsius: "))
# # Formula to convert Celsius to Fahrenheit
# fahreheit = (celsius * 9/5) + 32
# # Displaying result 
# print(f"\nTemperature in Fahrenheit: ", {fahreheit})


# Question: 
# Write a program that generates a random number between 1 and 100 and displays it as a "Lucky Number."
# import random  # Importing random module 
# # Generating a random number between 1 and 100 
# lucky_number = random.randint(1, 100)
# # Displaying the lucky number
# print("\nYour Lucky number is:", lucky_number)


# Question: 
# Write a program that takes two complex numbers as input and displays their sum and product. 
# # Taking complex number inputs from user
# num1 = complex(input("Enter First Complex Number: "))
# num2 = complex(input("Enter Second Complex Number: "))
# # Performing operations
# sum_result = num1 + num2
# product_result = num1 * num2
# # Displaying results
# print("\nSum: ", sum_result)
# print("Product: ", product_result)


# Question: 
# Write a program that takes a word from the user and prints the first and last characters of the word.
# Taking word input
# word = input("Entre the word: ")
# Extracting first and last character
# first_char = word[0]
# last_char = word[-1]
# Displaying results
# print("\nFirst Character: ", first_char)
# print("Last Character: ", last_char)


# Question: 
# Write a Python program that takes a sentence from the user and prints each character on a new line.
# Taking sentence input 
# sentence = input("Enter a sentence: ")
# Looping through each character 
# print("\nCharacters in Sentence")
# for char in sentence:
#     print(char)


# Question: 
# Write a program that takes a sentence and a word as input and checks if the word exists in the sentence. 
# Taking inputs 
# sentence = input("Enter the sentence: ")
# word = input("Enter the word: ")
# Checking if the word is in the sentence
# found = word in sentence
# Displaying result 
# print("\nWord found: ", found)


# Question: 
# Write a Python program that takes a sentence as input and counts the total number of characters in it.
# Taking sentence input 
# sentence = input("Enter the sentence: ")
# Calculating length of string 
# length = len(sentence)
# Displaying result 
# print("\nTotal Characters: ", length)


# Question: 
# Write a Python program that stores a famous quote in a multiline string and prints it.
# Storing a quote using multiline string 
# quote = """Success is not final, 
# failure is not fatal: 
# it is the courage to continue that counts.""" 
# Displaying the quote 
# print("\nFamous Quote:\n", quote)


# Question: 
# Write a Python program that takes a sentence and checks if a specific word is not present in it. 
# Taking sentence input 
# sentence = input("Enter a sentence: ")
# word_to_check = input("Enter a word to check: ")
# Checking if the word is not in the sentence 
# not_found = word_to_check not in sentence
# print("\nWord not found: ", not_found)


# A store owner wants to keep track of customer information. Write a Python program that: 
# • Takes a customer's name, age, and phone number as input. 
# • Displays all the details along with their data type.
# customer_name = input("Enter your name: ")
# customer_age = input("Enter your age: ")
# customer_number = input("Enter your phone number: ")
# customer_age = int(customer_age)
# print("\nCustomer name:", type(customer_name))
# print("\nCustomer age:", type(customer_age))
# print("\nCustomer number", type(customer_number))


# A restaurant needs to calculate the total bill amount, including tax. Write a program that: 
# • Takes the meal price as input. 
# • Calculates the total amount after adding 6% sales tax.
# price = float(input("Enter price: "))
# total =  price + (price * 0.06)
# print("\nTotal price: " , total)


# A banking system requires a random 6-digit OTP for authentication. Write a Python 
# program to generate and display a random OTP.
# import random
# otp = random.randint(100000, 999999)
# print("Your OTP is: ", otp)


# In electrical engineering, impedance is represented as a complex number. Write a Python program that: 
# • Takes two impedance values as complex numbers. 
# • Adds and multiplies them to get the resultant impedance. 
# v1 = complex(input("Enter value: "))
# v2 = complex(input("Enter value: "))
# v_sum = v1 + v2
# v_product = v1 * v2
# print(f"Sum: ", v_sum)
# print(f"product: ", v_product)


# A company assigns product codes such as "P1234X". Write a Python program that: 
# • Takes a product code as input. 
# • Extracts and displays the first letter and last letter separately. 
# code = input("Enter the product code (e.g., P1234X): ")
# first_letter = code[0]
# last_letter = code[-1]
# print(f"First Letter: ", first_letter)
# print(f"Last Letter: ", last_letter)


# A registration system requires the length of a user’s full name for validation. Write a Python program that: 
# • Takes a full name as input. 
# • Displays the total number of characters in the name. 
# name = input("Enter your name: ")
# lenght = len(name)
# print(f"Your name is: ", lenght)


# A company wants to filter product descriptions that contain a specific keyword. Write a Python program that: 
# • Takes a product description and a keyword as input. 
# • Checks if the keyword is present in the description. 
# description = input("Product description: ").lower()
# keyword = input("Enter keyword you search: ").lower()
# if keyword in description:
    # print("\nkeyword found in the description")
    
    
# A university wants to display motivational quotes in a structured format. Write a Python program that: 
# • Stores a three-line quote in a multiline string. 
# • Prints the quote with proper formatting.
# quote = """Consistence is the key to seccess
# keep hardworking
# you will be win"""
# print("\nQuote:" , quote)


# A shopping website wants to provide a random discount code to customers. Write a Python program that: 
# • Generates a random number between 1000 and 9999. 
# • Displays it as a discount code.
# import random
# code = random.randint(1000, 9999)
# print("\nYour discount code is: ", code)


# A company wants to identify negative reviews. Write a Python program that: 
# • Takes a customer review as input. 
# • Checks if the word "bad" is not present in the review. 
# customer_review = input("Please give reviews: ")
# word = input("Search keyword: ")
# if word not in customer_review:
    # print("\nThe review is positive or neutral")