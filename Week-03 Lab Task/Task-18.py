# Q18: Survey Response Frequency 
 
# A survey collected responses as a list of strings. Write a program to count how many times 
# each unique response appears. 

# Hint: 
# Consider iterating over the list and using the count() method for each unique response, or 
# explore using a dictionary to map responses to counts.

# Sample list of survey responses
responses = ["Yes", "No", "Yes", "Maybe", "Yes", "No", "Maybe"]

# Using count() method
unique_responses = set(responses)  # Get unique responses
for response in unique_responses:
    count = responses.count(response)  # Count each unique response
    print(f"Response: {response}, Count: {count}")


# Using Dictionary

# Sample list of survey responses
responses = ["Yes", "No", "Yes", "Maybe", "Yes", "No", "Maybe"]

# Using a dictionary to count frequencies
response_count = {}

for response in responses:
    if response in response_count:
        response_count[response] += 1  # Increment count if response already exists
    else:
        response_count[response] = 1  # Initialize count for new response

# Display the results
for response, count in response_count.items():
    print(f"Response: {response}, Count: {count}")
