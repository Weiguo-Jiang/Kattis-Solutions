C, K = list(map(int, input().split()))
n = int('1' + '0'*K)
floor = C // n * n
ceiling = (C // n + 1)*n
if C-floor == ceiling - C:
	print(ceiling)
elif C-floor < ceiling - C:
	print(floor)
else:
	print(ceiling)