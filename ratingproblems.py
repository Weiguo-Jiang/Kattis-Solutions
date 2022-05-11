n, k = list(map(int, input().split()))
s = 0
for i in range(k):
	a = int(input())
	s += a
print((s-(n-k)*3)/n, end=" ")
print((s+(n-k)*3)/n)