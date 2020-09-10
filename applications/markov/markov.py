import random

# Read in all the words in one go
with open('input.txt') as f:
    words = f.read()

# store the words in dictionary 
lookup_table = {}

# split
# [Cats and dogs and birds and fish dogs birds]
words_list = words.split()

for (word, next_word) in zip(words_list, words_list[1:]):
    if word not in lookup_table:
        lookup_table[word] = set()
        
    lookup_table[word].add(next_word)

print(lookup_table)


# TODO: construct 5 random sentences
# Your code here

