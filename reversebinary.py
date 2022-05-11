n = int(input())
l = list()
while n != 0:
	l.append(n%2)
	n //= 2
ans = 0
p = len(l)-1
for i in l:
	ans += i*(2**p)
	p -= 1
print(ans)