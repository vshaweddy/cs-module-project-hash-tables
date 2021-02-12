import random

# Read in all the words in one go
with open('input.txt') as f:
    words = f.read()

# store the words in dictionary 
lookup_table = {}

# split the sentences
# [Cats and dogs and birds and fish dogs birds]
words_list = words.split()

#
for (word, next_word) in zip(words_list, words_list[1:]):
    if word not in lookup_table:
        lookup_table[word] = set()
        
    lookup_table[word].add(next_word)

def choose_random(s):
    current_word = s

    # Check the last character of the current word if it's a stop word
    while current_word:
        print(current_word, end=" ")
        if current_word[-1] in set(".?!"):
            break

        current_word = random.choice(list(lookup_table[current_word]))

# to check if it's capital or has "
def get_start(word):
    return word[0].isupper() or (word[0] == '"' and word[1].isupper())

# possible start words
start_words = [word for word in filter(get_start, words_list)]

# repeat 5 sentences
for _ in range(5):
    start = random.choice(start_words)
    choose_random(start)
    print("\n")


