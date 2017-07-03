def f(a,b):
	print('From f()')
	for i in range(a):
		for j in range(b):
			print(i, j)
	return(a+b)
	
print(f(3,4))



