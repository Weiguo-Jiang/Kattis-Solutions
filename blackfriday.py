n = int(input())
inp = list(map(int, input().split()))
d = dict()
for i in inp:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

number = -1
for key, value in d.items():
	if value == 1 and key > number:
		number = key

if number == -1:
	print('none')
else:
	for i in range(n):
		if inp[i] == number:
			print(i+1)
			break