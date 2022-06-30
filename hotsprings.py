n = int(input())
t = sorted(list(map(int, input().split())))
l = list()
if n%2 == 0:
	for i in range(n//2):
		l.append(str(t[i]))
		l.append(str(t[-1-i]))
	l.reverse()
	print(" ".join(l))
else:
	for i in range(n//2):
		l.append(str(t[i]))
		l.append(str(t[-1-i]))
	l.append(str(t[n//2]))
	l.reverse()
	print(" ".join(l))