from itertools import chain, combinations

def powerSet(l):
    return chain.from_iterable(combinations(l, r) for r in range(len(l)+1))

T = int(input())
for i in range(T):
	print("Case #"+str(i+1)+":")
	d = dict()
	d1 = dict()
	inp = list(map(int, input().split()))
	l = list(powerSet(inp[1:20]))
	d[str(inp[-1])] = inp[-1]
	d1[inp[-1]] = 1

	ss = -1
	for i in l:
		if len(i) > 0 and len(i) < 20:
			l = list(i)
			s = sum(l)
			l = [str(ll) for ll in l]
			if i not in d:
				d[" ".join(l)] = s

			if s not in d1:
				d1[s] = 1
			else:
				d1[s] += 1
				ss = s
				break

	if ss == -1:
		print("Impossible")
	else:
		cnt = 0
		for key, value in d.items():
			if value == ss:
				print(key)
				cnt += 1
			if cnt == 2:
				break
