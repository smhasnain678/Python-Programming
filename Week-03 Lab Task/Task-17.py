# Q17: Social Media Post Likes Analysis 
 
# Given a list of like counts for several posts, sort the list and identify the post with the highest 
# number of likes. 


# Hint: 
# Sort the list (or use the max() function) to determine the highest like count, and practice 
# slicing if you need a subset of data.

# Sample list of like counts for various posts
like_counts = [120, 450, 320, 900, 750, 600]

# Sort the list of like counts
sorted_likes = sorted(like_counts)

# Identify the highest like count (last element in sorted list)
highest_likes = sorted_likes[-1:]

# Display the results
print("Sorted List of Like Counts:", sorted_likes)
print("Highest Like Count:", highest_likes)

