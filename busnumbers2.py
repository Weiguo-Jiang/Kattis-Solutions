Ramanujan = dict()
for i in range(1, 75):
	for j in range(i, 76):
		n = i**3 + j**3
		if n not in Ramanujan:
			Ramanujan[n] = 1
		else:
			Ramanujan[n] += 1

m = int(input())
if m < 1729:
	print("none")
else:
	ans = 1729
	for i in range(1730, m+1):
		if i in Ramanujan and Ramanujan[i] >= 2:
			ans = i
	print(ans)