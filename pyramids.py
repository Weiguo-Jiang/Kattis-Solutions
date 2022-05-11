N = int(input())
s = 0
h = 0
i = 1
while True:
	s += i**2
	if s <= N:
		h += 1
		i += 2
	else:
		break
print(h)