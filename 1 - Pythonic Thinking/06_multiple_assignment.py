"""Chapter 1: Pythonic Thinking"""

"""Item 6: Prefer Multiple Assignment Unpacking Over
           Indexing"""

snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190
}

items = tuple(snack_calories.items())
print(items)

item = ('Peanut butter', 'jelly')
first, second = item
print(first, 'and', second)

favourite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20)
}

((type1, (name1, cals1)),
  (type2,(name2, cals2)),
  (type3, (name3, cals3))) = favourite_snacks.items()

print(f'Favourite {type1} is {name1} with {cals1} calories')
print(f'Favourite {type2} is {name2} with {cals2} calories')
print(f'Favourite {type3} is {name3} with {cals3} calories')

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]

def list_of_snacks():
    snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
    for i in range(len(snacks)):
        item = snacks[i]
        name = item[0]
        calories = item[1]
        print(f'#{i+1}: {name} has {calories} calories')

def cleaner_list_of_snacks(snacks):
    for rank, (name, calories) in enumerate(snacks, 1):
        print(f'#{rank}: {name} has {calories} calories')


if __name__ == '__main__':
    names = ['pretzels', 'carrots', 'arugula', 'bacon']
    bubble_sort(names)
    print(names)
    
    snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
    list_of_snacks()
    print('\n')
    cleaner_list_of_snacks(snacks)