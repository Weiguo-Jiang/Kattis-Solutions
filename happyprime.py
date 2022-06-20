def prime(n):
	if n == 1:
		return 0
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return 0
	return 1


def happy(n):
	l = list()
	while True:
		s = 0
		while n != 0:
			mod = n % 10
			n //= 10
			s += mod**2
		n = s
		if s == 1:
			return 1
		elif s not in l:
			l.append(s)
		else:
			return 0


P = int(input())
for i in range(P):
	K, m = list(map(int, input().split()))

	flag = 1
	if not prime(m):
		flag = 0
	else:
		if not happy(m):
			flag = 0

	if flag:
		print(str(K) + " " + str(m) + " YES")
	else:
		print(str(K) + " " + str(m) + " NO")
