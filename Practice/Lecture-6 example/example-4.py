# Masking Sensitive Information

credit_card = "12345678900123456"

# Mask the fisrt 12 characters and show only the last 4 
masked_card = "**** **** **** " + credit_card[-4:]

print(masked_card)