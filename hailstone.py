def hailstone(n, s):
	if n == 1:
		s += n
		print(s)
		return

	if n % 2 == 0:
		s += n
		hailstone(n//2, s)
	else:
		s += n
		hailstone(3*n+1, s)

n = int(input())
s = 0
hailstone(n, s)