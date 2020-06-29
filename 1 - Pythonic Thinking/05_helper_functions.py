"""Chapter 1: Pythonic Thinking"""

"""Item 5: Write Helper Functions Instead of Complex
           Expressions"""

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)

print('Red:     ', my_values.get('red'))
print('Green:     ', my_values.get('green'))
print('Opacity:     ', my_values.get('opacity'))

# For query string 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f'Red:    {red!r}')
print(f'Green:    {green!r}')
print(f'Opacity:    {opacity!r}')

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    else:
        return default

if __name__ == '__main__':
    green = get_first_int(my_values, 'green')
