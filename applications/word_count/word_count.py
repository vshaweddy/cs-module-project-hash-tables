def word_count(s):
    lookup_table = {}
    # Replace the special characters with spacing
    for char in '":;,.-+=/\|[]{}()*^&\n':
        s = s.replace(char, ' ')
    
    # Lowercase all words
    s = s.lower()
    word_list = s.split()
    print(word_list)

    for word in word_list:
        if word not in lookup_table:
            lookup_table[word] = 0
        lookup_table[word] += 1
    return lookup_table


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))