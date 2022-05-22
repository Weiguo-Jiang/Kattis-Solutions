d = dict()
l = list()
l.append(list(map(int, input().split())))
l.append(list(map(int, input().split())))
l.append(list(map(int, input().split())))
for i in range(3):
	for j in range(3):
		d[l[i][j]] = [i, j]

s = 0
for i in range(1, 9):
	s += ((d[i][0] - d[i+1][0])**2 + (d[i][1] - d[i+1][1])**2)**0.5
print(s)