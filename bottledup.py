s, v1, v2 = list(map(int, input().split()))
p = s//v1
m = s//v2
for i in range(p+1):
	if (s-v1*i)%v2 == 0:
		b = (s-v1*i)//v2
		if b < m:
			m = b

if (s-m*v2)%v1 != 0:
	print("Impossible")
else:
	print((s-m*v2)//v1, m)