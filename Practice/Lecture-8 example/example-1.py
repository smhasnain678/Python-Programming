#List Comprehension

#Before List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango",]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
        
print(newList)


# After List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango",]

newList = [x for x in fruits if "a" in x]

print(newList)


# Example-01 List Comprehension
# Accessing List Items: Filtering Data

temperature = [28, 31, 29, 32, 30, 33, 27]
threshold = 30

# Access temperatures above the threshold   
high_temps = [temp for temp in temperature if temp > threshold]

print("Temperature above 30 C:", high_temps)

