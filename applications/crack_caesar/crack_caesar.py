# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('ciphertext.txt') as f:
    letters = f.read()

# Remove the special characters and numbers
alphanumeric = [e for e in letters if e.isalnum()]
alphabet = "".join([i for i in alphanumeric if not i.isdigit()])

# for char in '":;,.-+=/\|[]{}()*^&!\n':
#     letters = letters.replace(char, '')

# word_list = [char for char in letters]
# print(word_list)

# check each character frequency and store it in a dictionary
lookup_table = {}

for word in alphabet:
    if word not in lookup_table:
        lookup_table[word] = 0
    lookup_table[word] += 1

hash_list = lookup_table.items()

# sort it by value from high to low
s = sorted(hash_list, key = lambda x: (-x[1]))

# move the keys in an array one
keys_list = []

for key in s:
    keys_list.append(key[0])

# combine two arrays to one dictionary
values_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

print("Original key list is : " + str(keys_list)) 
print("Original value list is : " + str(values_list))

result = dict(zip(keys_list, values_list))
print(result)

# encode the ciphertext and return


