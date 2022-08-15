N, M, K = list(map(int, input().split()))
l = list()
for i in range(N):
	inp = [c for c in input()]
	l.append(inp)

ll = list()
for i in range(M):
	s = set()
	for j in l:
		s.add(j[i])
	if len(s) > 1:
		flag = 1
		for lll in ll:
			for j in s:
				if j in lll:
					lll |= s
					flag = 0
					break
			if not flag:
				break
		if flag:
			ll.append(s)

s = 0
for i in ll:
	s += len(i)-1
print(K-s)