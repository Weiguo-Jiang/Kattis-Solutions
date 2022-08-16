special = set()
for i in range(ord('!'), ord('*')+1):
	special.add(chr(i))
for i in range(ord('['), ord(']')+1):
	special.add(chr(i))

while True:
	try:
		n = int(input())
	except EOFError:
		break

	l = list()
	s = input()
	pw = 2**n-1

	for i in s:
		if i not in special:
			l.append(i)
		else:
			l.append('\\'*pw)
			l.append(i)
	print("".join(l))