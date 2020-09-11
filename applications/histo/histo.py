# Your code here

# Read in all the words in one go
with open('robin.txt') as f:
    words = f.read()

# Replace the special characters with spacing
for char in '":;,.-+=/\|[]{}()*^&\n':
    words = words.replace(char, ' ')

# create a dictionary to store the word as the key and the total as the value
lookup_table = {}

# Lowercase all words
words = words.lower()
word_list = words.split()

# count the frequency of the word
for word in word_list:
    if word not in lookup_table:
        lookup_table[word] = 0
    lookup_table[word] += 1

hash_list = lookup_table.items()

# sort from the value (number)
s = sorted(hash_list, key = lambda x: (-x[1], x[0]))

# create the histogram 
for key, value in s:
    print ('{:10}  {:10}'.format(key, value * "#"))