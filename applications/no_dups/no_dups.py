def no_dups(s):
    # Your code here
    lookup_table = set()
    
    # Lowercase all words
    s = s.lower()
    word_list = s.split()

    result = []

    for word in word_list:
        if word in lookup_table:
            continue
        else:
            lookup_table.add(word)
            result.append(word)
    
    return " ".join(result)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))