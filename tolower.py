P, T = list(map(int, input().split()))
cnt = 0
for i in range(P):
	flag = 1
	for j in range(T):
		s = input()
		for k in range(1, len(s)):
			if s[k] >= 'a' and s[k] <= 'z':
				continue
			else:
				flag = 0
	if flag:
		cnt += 1
print(cnt)