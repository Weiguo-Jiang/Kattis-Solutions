n = int(input())
l = list(map(int, input().split()))
ll = [0 for i in range(n+1)]
for i in l:
	if ll[i] == 0:
		ll[i-1] += 1
	else:
		ll[i-1] += 1
		ll[i] -= 1

arrows = 0
for i in range(n):
	arrows += ll[i]
print(arrows)