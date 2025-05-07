"""
✅ Part 9: Guided Mini Project — Word Analyzer Tool

🧩 Problem

Create a Python program that:

Takes a sentence from the user

Creates a dictionary with:

Each unique word as key

The length of each word as value

Also create a list of all vowels used (no duplicates)
"""

"""
Steps:
1: get sentence input
2: split into words
3: use dict comprehension for word: length
4: use set comprehension to get vowels
"""

sentence = input("Enter a sentence: ")
words = sentence.split()

word_lengths = {word: len(word) for word in words}
vowels_used = {ch for ch in sentence if ch in 'aeiouAEIOU'}

print("Word Lengths:", word_lengths)
print("Vowels Used:", vowels_used)