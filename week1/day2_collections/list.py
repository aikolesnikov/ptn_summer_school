l1 = []
l2 = [1, 2, 3, 'abc', True]
print(type(l2))

# list is like a string
print(l2[1])
print(l2[3:5])
print(l2)

l2[2] = 'qqq'
print(l2)

for i in l2:
    print(i)

print(l1)
l1 = l2
l2[1] = 222
print(l1)

l3 = l2.copy()
print(l3)
l2 = [1, 2, ['a', 'b', 'c'], 3]

print(l3)
import copy
l4 = copy.deepcopy(l2)
