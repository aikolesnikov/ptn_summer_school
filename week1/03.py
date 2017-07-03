import random

secret = random.randint(1, 3)

while True:
	try:
		your = int(input('your?:'))
	except ValueError:
		continue
		
	if your == secret:
		print('ok')
		break


