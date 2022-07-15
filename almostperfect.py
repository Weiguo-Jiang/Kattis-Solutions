def divisors(n):
	s = set()
	s.add(1)
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return sum(s)


while True:
	try:
		n = int(input())
	except EOFError:
		break

	s = divisors(n)

	if n == s:
		print(n, end=" perfect\n")
	elif abs(n-s) <= 2:
		print(n, end=" almost perfect\n")
	else:
		print(n, end=" not perfect\n")