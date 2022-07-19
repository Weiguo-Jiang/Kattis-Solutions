N, K = list(map(int, input().split()))
l = [0, 1, 1]
for i in range(N+1):
	l.append(l[-1]+l[-2])
while N > 2:
	if K > l[N-2]:
		K -= l[N-2]
		N -= 1
	else:
		N -= 2

print('N' if N == 1 else 'A')