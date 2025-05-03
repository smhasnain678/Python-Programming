#Sentence word analyzer

sentence = input("Enter a Sentence: ")

words = sentence.split()

print("\nWord Analysis")
for word in words:
    print(f"{word}: {len(word)} characters")