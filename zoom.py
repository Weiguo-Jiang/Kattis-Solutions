n, k = list(map(int, input().split()))
l = input().split()
ll = list()
for i in range(n):
	if (i+1)%k == 0:
		ll.append(l[i])
print(" ".join(ll))