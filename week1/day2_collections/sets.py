s1 = {1, 2, 3, 1}
print(type(s1))
print(s1)

s2 = {1, 4, 5, 6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

print([x * x for x in range(10) if x % 2])
print({x: x * x for x in range(10) if x % 2})
