"""Chapter 1: Pythonic Thinking"""

"""Item 4: Prefer Interpolated F-Strings Over C-style
           Format Strings and str.format"""

pantry = [
        ('avacados', 1.25),
        ('bananas', 2.5),
        ('cherries', 15)
    ]

# C-style
def c_style():
    a = 0b10111011
    b = 0xc5f
    print('Binary is %d, hex is %d' % (a,b))

    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %.2f' %(i, item, count))



# str.format
def format_style():
    a = 1234.5678
    formatted = format(a, ',.2f')
    print(formatted)

    key = 'my_var'
    value = 1.235

    formatted = '{:<10} = {:.2f}'.format(key, value)
    print(formatted)

    # specify the index of an argument
    formatted = '{1} = {0}'.format(key, value)
    print(formatted)


# f-string style 
def f_string_style():
    key = 'my_var'
    value = 1.234

    formatted = f'{key} = {value}'
    print(formatted)

    for i, (item, count) in enumerate(pantry):
        print(f'#{i+1}: '
              f'{item.title():<10s} = '
              f'{round(count)}')

if __name__ == '__main__':
    f_string_style()
