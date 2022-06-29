n = int(input())
p = 1
e = 1
for i in range(1, n+1):
	p *= i
	e += (1/p)
print(e)