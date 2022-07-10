N, p = list(map(int, input().split()))
t = list(map(int, input().split()))
if t[p] > 300:
	print("0 0")
else:
	cnt = 1
	time = t[p]
	penalty = t[p]
	t.pop(p)
	t.sort()

	for i in t:
		time += i
		if time > 300:
			break
		cnt += 1
		penalty += time
	print(cnt, penalty)
