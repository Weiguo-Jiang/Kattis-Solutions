def decimalToBase(n, b):
	l = list()
	while n != 0:
		l.append(str(n%b))
		n //= b
	
	l.reverse()
	return "".join(l)

while True:
	inp = input().split()
	if len(inp) == 1:
		break
	b, p, m = inp[0], inp[1], inp[2]

	b = int(b)

	p = int(p, base=b)
	m = int(m, base=b)
	rem = p%m
	if rem == 0:
		print(0)
	else:
		mod = decimalToBase(rem, b)
		print(mod)