"""Chapter 1: Pythonic Thinking"""

"""Item 8: Use zip to Process Iterators in Parallel"""

"""Things to Remember

* The zip built-in function can be used to iterate over multiple
  iterators in parallel.

* zip creates a lazy generator that produces tuples, so it 
  can be used on infinitely long inputs.

* zip truncates its output silently to the shortest iterator if you
  supply it with iterators of different lengths.

* Use the zip_longest function from ther itertools built-in module
  if you want to use zip on iterators of unequal lengths without
  truncation.
"""

import itertools

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

def indexing():
    longest_name = None
    max_count = 0

    for i in range(len(names)):
        count = counts[i]
        if count > max_count:
            longest_name = names[i]
            max_count = count

    print(longest_name)

def example_enumerate():
    longest_name = None
    max_count = 0

    for i, name in enumerate(names):
        count = counts[i]
        if count > max_count:
            longest_name = names[i]
            max_count = count

    print(longest_name)


def example_zip():
    longest_name = None
    max_count = 0
    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count
    print(longest_name)

def example_itertools():
    for name, count in itertools.zip_longest(names, counts):
        print(f'{name}: {count}')

def two_strings():
    group_1 = ['Adam', 'Bob', 'James', 'Geralt']
    group_2 = ['Josh', 'Lewis', 'Jacob']

    group_1.append('Jessie')
    for group1, group2 in itertools.zip_longest(group_1, group_2):
        print(f'Group 1 Names: {group1}\tGroup 2 Names: {group2}')

if __name__ == '__main__':
    indexing()
    example_enumerate()
    example_zip()
    example_itertools()
    two_strings()