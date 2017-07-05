print("HI")
a=2
b=3
c=4
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))*0.5
print("S =", S)
print()

ss="ImString"   # and Im comment
print(ss)
print("3rd char is: ", ss[3])
print("Last char is: ", ss[-1])
print("First is: ", ss[0])
print("Length: ", len(ss))
print("2-4 ", ss[1:4])
print("0-2 ", ss[:3])
print("3-end ", ss[3:])
print()

s2='17'
i2=int(s2)
print(int(s2)+1)
print("s2", type(s2))
print("i2", type(i2))
print()

a2=input('a2?')
b2=input('b2?')
print(a2+b2)
print(int(a2)+int(b2))
print()
