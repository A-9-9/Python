# iterable and iterator in python
from collections.abc import Iterator, Iterable
def g():
    yield 1


# Iterable -> can used in for loop
print(isinstance([], Iterable))
print(isinstance('abc', Iterable))
print(isinstance({}, Iterable))
print(isinstance(range(100), Iterable))
print(isinstance(10, Iterable))
print(isinstance(g(), Iterable))
print('='*30)

# Iterable -> can be invoke by next()
print(isinstance([], Iterator))
print(isinstance('abc', Iterator))
print(isinstance({}, Iterator))
print(isinstance(range(100), Iterator))
print(isinstance(10, Iterator))
print(isinstance(g(), Iterator))

print('='*30)

# can invoke iter() to transform iterable to iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(range(100)), Iterator))

# Iterator is a type of data flow, it can get date by invoke next() function, until there's no data
# data flow is lazy evaulation, delays the evaluation of an expression until its value is needed.