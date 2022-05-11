n = int(input())
for i in range(n):
	s = input()
	l = [j for j in s]
	sq = int(len(s)**0.5)
	for m in range(sq-1, -1, -1):
		k = m
		while k < len(s):
			print(s[k], end="")
			k += sq
	print()