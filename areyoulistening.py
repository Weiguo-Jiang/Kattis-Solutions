cx, cy, n = list(map(int, input().split()))
d = dict()
for i in range(n):
	x, y, r = list(map(int, input().split()))
	d[str(x)+" "+str(y)] = ((cx-x)**2+(cy-y)**2)**0.5-r

l = list()
cnt = 0
for key, value in d.items():
	l.append(value)
	if value < 0:
		cnt += 1
if cnt >= 3:
	print('0')
else:
	l = sorted(l)
	print(int(l[2]))