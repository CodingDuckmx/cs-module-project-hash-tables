def no_dups(s):
    # Your code here

    s = s.split(' ')

    dct = {word:s.count(word) for word in s if word.isspace() == False}

    new_string = ''

    for word in s:

        if dct[word] != 0:

            if new_string != '':
                new_string += (' ' + word)
            else:
                new_string += word
            dct[word] = 0
            
    return new_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))