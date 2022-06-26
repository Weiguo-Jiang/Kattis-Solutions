N = int(input())
E = int(input())

s = [set() for i in range(N+1)]
cnt = 0

for i in range(E):
	l = list(map(int, input().split()))[1:]
	if 1 in l:
		cnt += 1
		for j in l:
			s[j].add(i)
	else:
		share = set()
		for j in l:
			for k in s[j]:
				share.add(k)

		for j in l:
			s[j] = share.copy()

for i in range(N+1):
	if len(s[i]) == cnt:
		print(i)