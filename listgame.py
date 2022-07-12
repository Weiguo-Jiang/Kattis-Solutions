X = int(input())
l = list()
while X != 1:
	flag = 1
	for i in range(2, int(X**0.5)+2):
		if X % i == 0:
			flag = 0
			l.append(i)
			X //= i
			break
	if flag:
		l.append(X)
		break
print(len(l))