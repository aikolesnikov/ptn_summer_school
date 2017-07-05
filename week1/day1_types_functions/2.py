a = input('a?')
b = input('b?')
c = input('c?')

try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
		print('Invalid data.')
else:
	#Comment
	if a + b > c and b + c > a and a + c > b:
		p = ( a + b + c ) / 2
		S = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** 0.5
		print("S =", S)
		print()
	else:
		print("triangle does not exists")

print()
if a==b:
	print("yes")
elif a<b:
	print("no")
else:
	print("bigger")
	
i = 0 
while i<3:
	print(i)
	i=i+1