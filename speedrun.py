G, N = list(map(int, input().split()))
d = dict()
for i in range(N):
	st, et = list(map(int, input().split()))
	if et in d:
		d[et].append(st)
	else:
		d[et] = [st]

endTimes = list()
for i in sorted(d):
	for j in range(len(d[i])):
		endTimes.append(i)

startTimes = list()
for i in sorted(d):
	for j in d[i]:
		startTimes.append(j)

cnt = 1
time = endTimes[0]
for i in range(1, N):
	if startTimes[i] >= time:
		time = endTimes[i]
		cnt += 1

if cnt >= G:
	print("YES")
else:
	print("NO")