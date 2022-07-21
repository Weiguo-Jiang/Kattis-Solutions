from math import ceil
def isPrime(n):
	if n == 1 or n == 2:
		return True
	for i in range(2, ceil(n**0.5)+1):
		if n%i == 0:
			return False
	return True


def main():
	q = int(input())
	if q == 1:
		print("no")
	elif q == 2:
		print("yes")
	elif isPrime(q):
		print("yes")
	else:
		flag = 1
		for i in range(2, ceil(q**0.5)+1):
			if q%i == 0 and isPrime(i):
				c = i
				while i < q:
					i *= c
				if i == q:
					flag = 0
					print("yes")
					break
		if flag:
			print("no")


if __name__ == '__main__':
	main()