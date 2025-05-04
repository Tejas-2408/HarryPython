# s = {1,2,3,3,4,56,55,55,43,23}
# print(s)
# print(type(s))

# s.add(32)
# print(s)
# s.remove(2)
# s.discard(5)
# print(s)

## Sets operations
a = {1,2,3,4}
b = {3,4,5,6}

c=a.union(b)
print(c)
c = a.intersection(b)
print(c)
c = a-b # a.difference(b)
print(c)
