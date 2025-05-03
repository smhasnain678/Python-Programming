#Extracting Username from Email Addresses

email = "john.doe@gmail.com"

#Find the index of '@' and slice the string up to that point 
username = email[:email.index("@")]

print(username)