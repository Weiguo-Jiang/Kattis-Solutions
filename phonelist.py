def check(l):
	s = set()
	for i in l:
		if i in s:
			return 0
		for j in range(1, len(i)+1):
			s.add(i[:j])
	return 1



t = int(input())
for i in range(t):
	n = int(input())
	l = list()
	for j in range(n):
		l.append(input())
	l.sort(reverse=True)

	if check(l):
		print("YES")
	else:
		print("NO")