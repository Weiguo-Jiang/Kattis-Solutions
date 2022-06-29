n, m = list(map(int, input().split()))
l = list()
for i in range(1, n+1):
	l.append("T"+str(i))

for i in range(m):
	Ti, Tj = input().split()
	winnerIndex = l.index(Ti)
	loserIndex = l.index(Tj)

	if winnerIndex > loserIndex:
		c = l[loserIndex]
		for j in range(loserIndex, winnerIndex):
			l[j] = l[j+1]
		l[winnerIndex] = c
print(" ".join(l))