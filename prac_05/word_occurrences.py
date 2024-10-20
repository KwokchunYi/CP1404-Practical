"""
Word Occurrences
Estimate: 25 minutes
Actual: 30 minutes
"""

# Get the input string from the user
text = input("Text: ")

# Split the input text into words and create an empty dictionary
word_counts = {}
words = text.split()

# Count occurrences of each word
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Find the length of the longest word for alignment
longest_word_length = max(len(word) for word in word_counts)

# Sort the dictionary by the word (key) and print the results
for word in sorted(word_counts):
    print(f"{word:{longest_word_length}} : {word_counts[word]}")
