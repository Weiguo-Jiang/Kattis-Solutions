from math import ceil

def isPrime(n):
	if n == 1 or n == 2:
		return True
	for i in range(2, ceil(n**0.5)+1):
		if n%i == 0:
			return False
	return True


def factor(n):
	l = list()
	while True:
		if isPrime(n):
			l.append(n)
			break
		for i in range(2, ceil(n**0.5)+1):
			if n % i == 0:
				l.append(i)
				n //= i
				break
	return sum(l)


while True:
	n = int(input())
	if n == 4:
		break

	cnt = 1
	while True:
		if isPrime(n):
			print(n, end=" ")
			print(cnt)
			break
		else:
			n = factor(n)
			cnt += 1
