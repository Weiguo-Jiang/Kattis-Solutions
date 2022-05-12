P = int(input())
for i in range(P):
	K, b, n = list(map(int, input().split()))
	print(str(K), end=" ")
	s = 0
	while n != 0:
		s += (n%b)**2
		n //= b
	print(s)