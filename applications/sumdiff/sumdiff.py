"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import itertools

#q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

Q = {(a,b,d) : a+b+d+3 for a,b,d in itertools.product(q,repeat=3)}

for c in q:

  for keys, value in Q.items():

    if value == c:

      a,b,d = keys
  
      print(f'f({a}) + f({b}) = f({c}) - f({d})'
        f'    {f(a)} + {f(b)} = {f(c)} - {f(d)}')   
