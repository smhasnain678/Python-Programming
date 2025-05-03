#Random Password Generator

import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

password_length = int(input("Enter password length: "))

password = ""
for _ in range(password_length):
    password += random.choice(characters)
    
print("\nGenerated password: ", password)
