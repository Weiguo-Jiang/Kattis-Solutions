n = int(input())
l = list(reversed(sorted(list(map(int, input().split())))))
A = 0
B = 0
for i in range(n):
	if i % 2 == 0:
		A += l[i]
	else:
		B += l[i]

print(str(A) + " " + str(B))