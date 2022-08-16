n = int(input())
for i in range(n):
	s = input()
	m = 1
	while True:
		ss = s[0:m]
		if len(s) % m == 0:
			if ss*(len(s)//m) == s:
				break
		else:
			if ss*(len(s)//m) + ss[0:len(s)%m] == s:
				break
		m += 1
	print(m)