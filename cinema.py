N, M = list(map(int, input().split()))
groups = list(map(int, input().split()))
cnt = 0
cap = 0
for i in range(M):
	cap += groups[i]
	if cap > N:
		cap -= groups[i]
		continue
	cnt += 1
print(M-cnt)