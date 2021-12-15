# compare mutable object and immutable object.
# mutable is like [list], {dict}, (set).
# immutable is like 'str', int, float, (tuple).
# when mutable object change(assign), it only modify the value of the object.
# when modify the immutable object, it change the pointer to point the new memory address.

# mutable
li = [1, 2, 3]
li2 = li

print(li)
print(li2)
print("id(li) == id(li2) ?", id(li) == id(li2))
print('='*30)
li[0] = -1
print(li)
print(li2)
print("id(li) == id(li2) ?", id(li) == id(li2))
print('='*30)

# immutable
s = 'abc'
s1 = s

print(s)
print(s1)
print("id(s) == id(s1) ?", id(s) == id(s1))
print('='*30)
s = 'zzz'
print(s)
print(s1)
print("id(s) == id(s1) ?", id(s) == id(s1))
print('='*30)