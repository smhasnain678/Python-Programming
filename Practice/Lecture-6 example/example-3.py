#Extracting Username, Domain, and Extension from Email Addresses

email = "smhasnain43@gmail.com"

# Extract the username (email base)
username = email[:email.index("@")] #Slices from start to the character before '@'
print("Email base:", username) 

# Extract the domain and extension
domain_and_extension = email[email.index("@") + 1:] # Slice from after '@' to the end 
print("Domain and extension:", domain_and_extension)

# Split Domain and Extension into separate parts
domain = domain_and_extension[:domain_and_extension.index(".")] # Slices from start to before '.'

# Slices from after '.' to end
extension = domain_and_extension[domain_and_extension.index(".") + 1:]
print("Domain:", domain)

print("Extension:", extension)