d = {}
print(type(d))

d['a']=1
d[2]='b'
print(d)

d[(1,2,3)]='c'
print(d)
print(d[1,2,3])

phonebook = {'name1':911, 'name2':922}
print(phonebook['name1'])
phonebook['name2']=933
print(phonebook)

print(d.items())