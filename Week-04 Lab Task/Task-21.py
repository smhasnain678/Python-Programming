# Q9: Find New Users 
 
# You have a set of old usernames and a list of new users. Identify which users are new. 

# Hint: Use set difference between the new and old user sets.

# Set of old usernames
old_users = {"ali", "sara", "usman", "fatima"}

# List of new users (some may be old)
new_users = ["sara", "usman", "bilal", "zainab", "ahmed"]

# Convert new_users to a set
new_users_set = set(new_users)

# Use set difference to find truly new users
new_only = new_users_set - old_users

# Display result
print("New Users:")
for user in new_only:
    print(user)
