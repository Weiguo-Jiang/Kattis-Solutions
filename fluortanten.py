n = int(input())
queue = [i for i in list(map(int, input().split())) if i != 0]
s = 0
for i in range(n-1):
	s += queue[i]*(i+1)

m = 0
cur = 0
for i in range(n-2, -1, -1):
	cur += queue[i]
	if cur > m:
		m = cur
print(m+s)
