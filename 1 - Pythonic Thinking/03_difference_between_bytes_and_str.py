"""Chapter 1: Pythonic Thinking"""

"""Item 3: Know the Difference Between bytes and str"""

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of bytes

a = b'h\x65llo'
print(list(a))
print(a)

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))


"""Writing to files"""

with open('data.txt', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

with open('data.txt', 'rb') as f:
    data = f.read()
    print(repr(to_bytes(data)))
