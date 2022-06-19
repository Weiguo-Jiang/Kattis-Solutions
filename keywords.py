n = int(input())
s = set()
for i in range(n):
	l = [i for i in input().lower()]
	for j in range(len(l)):
		if l[j] == '-':
			l[j] = " "
	s.add("".join(l))
print(len(s))