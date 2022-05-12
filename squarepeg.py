L, R = list(map(int, input().split()))
if 2*R >= 2**0.5*L:
	print('fits')
else:
	print('nope')