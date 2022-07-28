from math import ceil

def prime(n):
	if n == 1 or n == 2:
		return True
	for i in range(2, ceil(n**0.5)+1):
		if n%i == 0:
			return False
	return True



while True:
	n = int(input())
	if n == 0:
		break

	flag = not prime(n)
	lower = 2*n+1

	while True:
		if prime(lower):
			break
		else:
			lower += 1

	if flag:
		print(str(lower) + " (" + str(n) + " is not prime)")
	else:
		print(lower)