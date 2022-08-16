d = dict()
d['0'] = 0
d['1'] = 1
d['2'] = 2
d['3'] = 3
d['4'] = 4
d['5'] = 5
d['6'] = 6
d['7'] = 7
d['8'] = 8
d['9'] = 9
d['a'] = 10
d['b'] = 11
d['c'] = 12
d['d'] = 13
d['e'] = 14
d['f'] = 15

def hex2Decimal(s):
	pw = len(s)-1
	n = 0
	for i in s:
		n += d[i.lower()]*(16**pw)
		pw -= 1
	return n


while True:
	try:
		s = input()
	except EOFError:
		break

	start = list()
	for i in range(0, len(s)-2):
		if s[i:i+2].lower() == '0x' and s[i+2].lower() in d:
			start.append(i)

	l = list()
	for i in start:
		j = i + 2
		while j < len(s):
			if s[j].lower() in d and len(l) != 8:
				l.append(s[j])
			else:
				print(s[i:j], end=" ")
				print(hex2Decimal("".join(l)))
				l = list()
				break
			j += 1
		if len(l) != 0:
			print(s[i:j], end=" ")
			print(hex2Decimal("".join(l)))
			l = list()
