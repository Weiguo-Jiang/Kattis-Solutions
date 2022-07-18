n = int(input())
l = list()
for i in range(n):
	c = int(input())
	l.append(c)
l.sort()
l.reverse()

H = 0
for i in range(n):
	if l[i] >= i+1:
		H = i+1
	else:
		break
print(H)