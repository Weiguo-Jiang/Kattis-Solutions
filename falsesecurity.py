l1 = [chr(i) for i in range(65, 91)] + ['_', ',', '.', '?']
l2 = ['.-', '-...', '-.-.', '-..', '.', '..-.',
	  '--.', '....', '..', '.---', '-.-', '.-..',
	  '--', '-.', '---', '.--.', '--.-', '.-.',
	  '...', '-', '..-', '...-', '.--', '-..-',
	  '-.--', '--..', '..--', '.-.-', '---.', '----']

d1 = dict()
d2 = dict()
for i in range(len(l1)):
	d1[l1[i]] = l2[i]
	d2[l2[i]] = l1[i]

while True:
	try:
		inp = [c for c in input()]
	except EOFError:
		break

	l1 = list()
	l2 = list()

	for c in inp:
		l1.append(d1[c])
		l2.append(len(d1[c]))

	s = "".join(l1)
	l2.reverse()
	decoded = list()
	index = 0
	for i in l2:
		decoded.append(s[index:index+i])
		index += i

	for i in range(len(decoded)):
		decoded[i] = d2[decoded[i]]

	print("".join(decoded))