def binaryToOctal(binary):
	octal = -1
	if binary == "000":
		octal = '0'
	elif binary == "001":
		octal = '1'
	elif binary == "010":
		octal = '2'
	elif binary == "011":
		octal = '3'
	elif binary == "100":
		octal = '4'
	elif binary == "101":
		octal = '5'
	elif binary == "110":
		octal = '6'
	elif binary == "111":
		octal = '7'
	return octal


inp = [i for i in input()]
if len(inp) % 3 == 0:
	l = list()
	for i in range(0, len(inp), 3):
		l.append(binaryToOctal("".join(inp[i:i+3])))
	print("".join(l))
else:
	l = list()
	inp.reverse()
	for i in range((len(inp)//3+1)*3-len(inp)):
		inp.append('0')
	inp.reverse()

	for i in range(0, len(inp), 3):
		l.append(binaryToOctal("".join(inp[i:i+3])))
	print("".join(l))