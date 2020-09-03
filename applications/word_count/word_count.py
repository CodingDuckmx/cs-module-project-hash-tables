def word_count(s):
    # Your code here

    s = s.lower().split()

    ignored = set(x for x in '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' '))


    for i in range(len(s)):

        if s[i][0] in ignored:

            s[i] = s[i][1:]

        if s[i][-1] in ignored:

            s[i] = s[i][:-1]
    
        try:
            
            if s[i][1] in ignored:

                s.pop(i)

        except:

            continue



    dct = {word : s.count(word) for word in s if word not in ignored}

    return dct

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello    hello"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))