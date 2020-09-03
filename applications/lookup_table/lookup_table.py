import math
import random
import time
# Your code here

pow_dct = {}
fact_dct = {}
div_dict = {}
mod_dict = {}

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    
    # if (x,y) not in pow_dct:

    #     pow_dct[(x,y)] = math.pow(x, y)
    
    # v = pow_dct[(x,y)]

    # if v not in fact_dct:

    #     fact_dct[v] = math.factorial(v)

    # v = fact_dct[v]

    # if v not in div_dict:

    #     div_dict[v] = v // (x+y)

    # v = div_dict[v]

    # if v not in mod_dict:

    #     mod_dict[v] = v % 982451653

    # return mod_dict[v]

    if (x,y) not in cache:

        cache[(x,y)] = slowfun_too_slow(x, y)
    
    return cache[(x,y)] 


if __name__ == "__main__":

    start = time.time()
    for i in range(50000):
        x = random.randrange(2, 14)
        y = random.randrange(3, 6)
        print(f'{i}: {x},{y}: {slowfun(x, y)}')
    
    end = time.time()

    print('##############################')
    print(end-start)
    print('##############################')
