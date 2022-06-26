P = int(input())
for i in range(P):
	c, n = list(map(int, input().split()))
	octal = 0
	hexadecimal = 0
	decimal = n

	pw = 0
	while n != 0:
		mod = n % 10
		if mod >= 8:
			octal = 0
			break
		octal += (mod*(8**pw))
		pw += 1
		n //= 10

	n = decimal

	pw = 0
	while n != 0:
		mod  = n % 10
		hexadecimal += (mod*(16**pw))
		pw += 1
		n //= 10
	print(c, octal, decimal, hexadecimal)