# Your code here

with open('robin.txt') as f:
    script = f.read()



def word_count(s):
    # Your code here

    s = s.lower().split()

    ignored = set(x for x in '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' '))


    for i in range(len(s)):

        if s[i][0] in ignored:

            s[i] = s[i][1:]

        if s[i][-1] in ignored:

            s[i] = s[i][:-1]
    
        # second round in case like ."
        if s[i][-1] in ignored:

            s[i] = s[i][:-1]

        try:
            
            if s[i][1] in ignored:

                s.pop(i)

        except:

            continue



    dct = {word : s.count(word) for word in s if word not in ignored}

    return dct

dct = word_count(script)


def getKey(item):

  return item[1]

lst = list(dct.items())

ordered_dct = {}

for item in lst:

  if item[1] not in ordered_dct:

    ordered_dct[item[1]] = []
  
  ordered_dct[item[1]].append(item[0])

for inner_list in ordered_dct:

  ordered_dct[inner_list] = sorted(ordered_dct[inner_list])

ordered_keys = sorted(ordered_dct.keys())

max_length = 0
longest_word = None

for word in dct.keys():

  if len(word)>max_length:

    longest_word = word
    max_length = len(word)

for i in range(1,len(ordered_keys)+1):
  for word in ordered_dct[ordered_keys[-i]]:

    print(word,' '*(len(longest_word)-len(word)+2), '#'*ordered_keys[-i])
