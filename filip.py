a, b = input().split()
a = list(a)
a1 = ""
b1 = ""
for i in range(len(a)-1, -1, -1):
	a1 += a[i]
	b1 += b[i]
print(max(int(a1), int(b1)))