k = int(input())
l = list()
for i in range(k):
	year = 2022
	y, c1, c2 = list(map(int, input().split()))
	while True:
		if (year - y) % c1 == 0 and (year - y) % c2 == 0:
			break
		else:
			year += 1
	l.append(year)
print(min(l))