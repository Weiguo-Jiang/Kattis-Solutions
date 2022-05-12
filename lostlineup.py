n = int(input())
l = list(map(int, input().split()))
d = dict()
for i in range(n-1):
	d[l[i]] = i+2
print("1", end=" ")
for i in range(n-1):
	print(d[i], end=" ")
print()