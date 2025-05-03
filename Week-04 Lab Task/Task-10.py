# Q10: Set Membership Checker 
 
# Check if a username already exists in the system using a set. 

users = {"admin98", "Harry", "Sara"}

new_users = input("Enter your name")

if new_users in users:
    print("Username already exits: ")
else:
    print("Username is available")