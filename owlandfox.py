def sumOfDigits(n):
	s = 0
	while n != 0:
		s += n % 10
		n //= 10
	return s

n = int(input())
for i in range(n):
	N = int(input())
	s = sumOfDigits(N)-1
	while True:
		s1 = sumOfDigits(N)
		if s1 == s:
			print(N)
			break
		else:
			N -= 1
