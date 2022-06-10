op = []
while True:
	n = int(input())
	if n == 0:
		op.pop()
		break
	l = list()
	for i in range(n):
		name = input()
		l.append(name)
	for i in range(n):
		for j in range(n-i-1):
			if l[j][0:2] > l[j+1][0:2]:
				c = l[j+1]
				l[j+1] = l[j]
				l[j] = c
	for i in l:
		op.append(i)
	op.append('\n')

for i in op:
	if i == '\n':
		print(i, end="")
	else:
		print(i)