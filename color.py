S, C, K = list(map(int, input().split()))
l = sorted(list(map(int, input().split())))
value = l[0]
cnt = 1
cap = 0
for i in range(S):
	cap += 1
	if cap > C:
		cap = 1
		cnt += 1
		value = l[i]

	if abs(l[i]-value) > K:
		value = l[i]
		cnt += 1
		cap = 1

print(cnt)