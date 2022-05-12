n = int(input())
l = list()
cnt = 0
for i in range(n):
	u, t = input().split()
	if u not in l:
		print(u + " " + t)
		l.append(u)
		cnt += 1
	if cnt == 12:
		break