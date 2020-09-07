# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('ciphertext.txt') as f:
    script = f.read()

dct = {}

script = script.replace('\n',' ')


for i in script:

    if (i.isalpha() == False) or (i.isupper() == False):

        continue

    if i not in dct:

        dct[i] = 0
    
    dct[i] += 1

def getKey(item):

  return item[1]

alphabet = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
final_dct = {letter:None for letter in alphabet}

sorted_dict = sorted(dct.items(),key=getKey)

for i in range(1,27):

   final_dct[sorted_dict[i-1][0]] = alphabet[-i]

new_script = ''

for i in script:

    if i in final_dct:

        new_script += final_dct[i]
    
    else:

        new_script += i

print(new_script)
