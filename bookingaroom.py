n, r = list(map(int, input().split()))
if n == r:
	print("too late")
else:
	s = set()
	for i in range(1, n+1):
		s.add(i)
	for i in range(r):
		inp = int(input())
		s.remove(inp)
	l = list(s)
	print(l[0])