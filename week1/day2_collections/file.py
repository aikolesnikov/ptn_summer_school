f = open('1.txt', 'wt')

f.write('str1\n')
f.write('str2\n')
print(f.name)
print()

f.close()

f = open('1.txt', 'rt')
s = f.read()
print(s)
f.close()


f = open('1.txt', 'rt')
for line in f:
    print(line)
f.close()

f = open('1.txt', 'rt')
for index, line in enumerate(f):
    if index == 1:
        break
f.close()

# !! use this way
with open('1.txt', 'rt') as f:
    for line in f:
        print(line)
