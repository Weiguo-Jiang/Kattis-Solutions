n = int(input())
d = dict()
d[0] = 1
for i in range(n+1):
	d[i+1] = d[i]*(4*i+2)//(i+2)
print(d[n+1])