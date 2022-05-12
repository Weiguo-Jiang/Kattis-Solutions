n = int(input())
for i in range(n):
	a = input()
	b = input()
	print(a)
	print(b)
	for j in range(len(a)):
		if a[j] == b[j]:
			print('.', end="")
		else:
			print('*', end="")
	print('\n')