import random

secret = random.randint(1, 3)
tries = 0


while tries<5:
# while True:
	try:
		your = int(input('your?:'))
	except ValueError:
		continue
		
	tries +=1
	if your == secret:
		print('ok')
		print(tries, 'tries')
		break
else:
	print("???")

