import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

words = words.replace('\n',' ')


# Get all the possible words.


# soup = set(words.lower().split())

# print(len(soup))

# temp_soup = soup.copy()

# for word in soup:

#     # if word.isalnum():

#     #     continue
    
#     if (word.isalnum() == False):

#         temp_soup.remove(word)
#         continue

#     if (word[0].isalnum() == False):

#         temp_soup.remove(word)
#         temp_soup.add(word[1:])

#     if (word[0-1].isalnum() == False):

#         temp_soup.remove(word)
#         temp_soup.add(word[:-1])
    
# soup = temp_soup

#### Second try.

soup = list(set(words.split(' ')))

splitted_sentence = words.split()

start_soup = {word for word in soup if word.istitle()}

# stop_soup = {word for word in soup if word[-1] in {'.','?','!'}}

following = {word : [] for word in soup}

for i in range(len(splitted_sentence)-1):

    following[splitted_sentence[i]].append(splitted_sentence[i+1])



# TODO: construct 5 random sentences
# Your code here



def add_following_word(word,following):

    new_word = random.choice(following[word])

    following[word].remove(new_word)
    if following[word] == []:

        following[word].append('') 

    return new_word

def write_script(soup, initial_word,length):

    new_script = initial_word + ' '

    for _ in range(length):

        new_word = add_following_word(new_script.split()[-1],following)
        new_script += new_word + ' '

        try:
            if new_word[-1] in {'.','!','?'} or new_word[-2] in {'.','!','?'}:

                break

        except:

            continue

    return new_script

for _ in range(5):

    initial_word = random.choice(list(start_soup))

    length = random.randint(0,len(soup)-1)

    print(write_script(soup, initial_word,length))
    print('')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('')

# print(None in list(start_soup))