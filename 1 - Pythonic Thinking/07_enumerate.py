"""Chapter 1: Pythonic Thinking"""

"""Item 7: Prefer enumerate Over range"""

"""Things to Remember

* enumerate provides concise syntax for looping over an iterator
  and getting the index of each item from the iterator as you go.

* Prefer enumerate instead of looping over a range and indexing
  into a sequence

* You can supply a second parameter to enumerate to specify the
  number from which to begin counting (zero is default)
"""

from random import randint

flavour_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

def bitwise():
    random_bits = 0
    for i in range(32):
        if randint(0, 1):
            random_bits |= 1 << i

    print(bin(random_bits)) 

def flavours_basic():
    for flavour in flavour_list:
        print(f'{flavour} is delicious')
    
def flavours_rank():
    for i in range(len(flavour_list)):
        flavour = flavour_list[i]
        print(f'{i + 1}: {flavour}')

def flavours_iter():
    for i, flavour in enumerate(flavour_list, 1):
        print(f'{i}: {flavour}')

if __name__ == '__main__':
    flavours_basic()
    print('\n')
    flavours_rank()
    print('\n')
    flavours_iter()