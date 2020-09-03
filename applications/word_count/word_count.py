def word_count(s):
    # Your code here

    dct = {}

    s = s.lower().split()

    ignored = set(x for x in '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' '))

    # if set(s).intersection(ignored) != {}:

    #     for symbol in ignored:

    #         if symbol in s:

    #             s.replace(symbol,'')

    

    for word in s:

        if word == '' or word in ignored:
            continue

        if word not in dct:

            dct[word] = 0
        
        dct[word] +=1

    return dct


    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello    hello"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))