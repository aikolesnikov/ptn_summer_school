s = "TRY"
for c in s:
    print(c)

print(s.encode('utf8'))

print(dir(s))
print(s.upper())
print(s.count('T'))
print(s.replace('R', '*'))
print(s.upper())
print(s.endswith('Y'))

s = '1,2,3,4'
print(s.split(','))
print(s.split('2'))

name = 'kaim'
age = 55
print('name=' + name + ', age:' + str(age))
"Name: %s; age: %d", name, age

# f"Name: {name}; age: {age}"