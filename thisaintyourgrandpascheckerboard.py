n = int(input())
l = list()
flag = 1
for i in range(n):
	inp = input()
	if "BBB" in inp or "WWW" in inp:
		flag = 0
	W = 0
	B = 0
	for i in inp:
		if i == 'W':
			W += 1
		else:
			B += 1
	if W != B:
		flag = 0
	l.append(inp)

for i in range(n):
	W = 0
	B = 0
	col = ""
	for j in l:
		if j[i] == 'W':
			W += 1
		else:
			B += 1
		col += j[i]
	if W != B:
		flag = 0
	if "BBB" in col or "WWW" in col:
		flag = 0

print(flag)