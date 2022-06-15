p, q = list(map(int, input().split()))
inp = input().lower()
if inp == 'aabb':
	if q < 7:
		print('-1')
	else:
		print('8 9')
elif inp == 'abab':
	if q-p > 2 or q < 8:
		print('-1')
	else:
		print('7 9')
elif inp == 'abba':
	if q-p > 3:
		print('-1')
	else:
		print(p+1, end=" ")
		print(q-1)
elif inp == 'baab':
	if p > 2 or q < 8:
		print('-1')
	else:
		print('1 9')
elif inp == 'baba':
	if p > 2 or q-p > 2:
		print('-1')
	else:
		print('1 ', end="")
		print(p+1)
elif inp == 'bbaa':
	if p > 3:
		print('-1')
	else:
		print('1 2')