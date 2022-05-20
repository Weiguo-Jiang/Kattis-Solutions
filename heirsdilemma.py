def check(n):
	if '0' in str(n):
		return 0
	s = set()
	for i in str(n):
		s.add(int(i))
	if len(s) != len(str(n)):
		return 0
	for i in s:
		if n % i != 0:
			return 0
	return 1

cnt = 0
L, H = list(map(int, input().split()))
for i in range(L, H+1):
	cnt += check(i)

print(cnt)