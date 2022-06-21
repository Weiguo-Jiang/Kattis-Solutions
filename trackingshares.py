C = int(input())
days = set()
lll = list()
for i in range(C):
	ll = list()
	records = int(input())
	for j in range(records):
		l = list(map(int, input().split()))
		days.add(l[1])
		ll.append(l)
	lll.append(ll)
days = sorted(list(days))

for d in days:
	shares = 0
	for i in lll:
		latest = -1
		day = -1
		for j in range(len(i)):
			if i[j][1] <= d and i[j][1] > day:
				day = i[j][1]
				latest = i[j][0]
		
		if latest != -1:
			shares += latest
	print(shares)
