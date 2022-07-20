T = int(input())
for i in range(T):
	N = int(input())
	l = sorted(list(map(int, input().split())), reverse=True)
	index = 1
	s = 0
	while N != 0 and index < len(l):
		s += l[index]
		index += 2
		N -= 1
	print(s)