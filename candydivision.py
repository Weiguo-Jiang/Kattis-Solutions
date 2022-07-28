from math import ceil

def divisors(n):
	l = list()
	i = 1
	while i**2 <= n:
		if n%i == 0:
			l.append(i-1)
			l.append(n//i-1)
		i += 1
	return l


N = int(input())
l = divisors(N)
l = list(set(l))
l = [str(i) for i in sorted(l)]
print(" ".join(l))