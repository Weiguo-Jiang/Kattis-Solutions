from math import e, pi, log10, floor
while True:
	try:
		n = int(input())
	except EOFError:
		break

	if n <= 1:
		print("1")
	else:
		d = (n*log10(n/e)+log10(2*pi*n)/2)
		print(floor(d)+1)