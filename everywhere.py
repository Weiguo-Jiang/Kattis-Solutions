n = int(input())
for i in range(n):
	k = int(input())
	s = set()
	for j in range(k):
		c = input()
		s.add(c)
	print(len(s))