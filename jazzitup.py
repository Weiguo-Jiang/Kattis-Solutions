def squareFree(num):
	square = int(num**0.5)
	for i in range(2, square):
		if num % (i**2) == 0:
			return 0
	return 1


n = int(input())
for m in range(2, n):
	num = m*n
	if squareFree(num):
		print(m)
		break