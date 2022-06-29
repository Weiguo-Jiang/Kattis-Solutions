import math
p, a, b, c, d, n = list(map(int, input().split()))
l = list()
for i in range(1, n+1):
	price = p*(math.sin(a*i+b)+math.cos(c*i+d)+2)
	l.append(price)

differences = list()
for i in range(n-1):
	differences.append(l[i+1]-l[i])

maximumDecline = 0
cur = 0
for i in range(n-1):
	cur += differences[i]
	if cur < maximumDecline:
		maximumDecline = cur

	if cur > 0:
		cur = 0
print(abs(maximumDecline))