n = int(input())
m = 1
for i in range(2, int(n**(1/9))+2):
	if n % (i**9) == 0:
		m = i
print(m)