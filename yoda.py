inp1 = int(input())
inp2 = int(input())
l1 = list()
l2 = list()
while inp1 != 0 and inp2 != 0:
	mod1 = inp1 % 10
	mod2 = inp2 % 10
	if mod1 > mod2:
		l1.append(str(mod1))
	elif mod1 < mod2:
		l2.append(str(mod2))
	else:
		l1.append(str(mod1))
		l2.append(str(mod2))
	inp1 //= 10
	inp2 //= 10

if inp1 == 0 and inp2 == 0:
	if len(l1) == 0:
		print("YODA")
	else:
		l1.reverse()
		print(int("".join(l1)))

	if len(l2) == 0:
		print("YODA")
	else:
		l2.reverse()
		print(int("".join(l2)))
elif inp1 == 0:
	if len(l1) == 0:
		print("YODA")
	else:
		l1.reverse()
		print(int("".join(l1)))

	print(inp2, end="")
	l2.reverse()
	print(int("".join(l2)))
else:
	print(inp1, end="")
	l1.reverse()
	print(int("".join(l1)))

	if len(l2) == 0:
		print("YODA")
	else:
		l2.reverse()
		print(int("".join(l2)))
