N, M = list(map(int, input().split()))
s = set()
d = dict()
for i in range(M):
	inp = input()
	s.add(inp)
	d[inp] = i+1

l = list()
flag = 1
for i in range(1, N):
	route1 = str(i) + " " + str(i+1)
	route2 = str(i+1) + " " + str(i)
	if (route1 not in s) and (route2 not in s):
		flag = 0
		break
	else:
		if route1 in d:
			l.append(d[route1])
		else:
			l.append(d[route2])

home1 = "1 " + str(N)
home2 = str(N) + " 1"
if (home1 not in s) and (home2 not in s):
	flag = 0
else:
	if home1 in s:
		l.append(d[home1])
	else:
		l.append(d[home2])

if flag:
	for i in l:
		print(i)
else:
	print("impossible")