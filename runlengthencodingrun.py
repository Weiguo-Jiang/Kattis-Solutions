I, s = input().split()
if I == 'E':
	c = s[0]
	cnt = 0
	for i in range(len(s)):
		if s[i] == c:
			cnt += 1
		else:
			print(c, end="")
			print(cnt, end="")
			c = s[i]
			cnt = 1
	print(c, end="")
	print(cnt)
else:
	for i in range(0, len(s)-1, 2):
		print(s[i]*int(s[i+1]), end="")
	print()
