l = ['zero',
	 'one',
	 'two',
	 'three',
	 'four', 
	 'five',
	 'six',
	 'seven',
	 'eight',
	 'nine',
	 'ten',
	 'eleven',
	 'twelve',
	 'thirteen',
	 'fourteen',
	 'fifteen',
	 'sixteen',
	 'seventeen',
	 'eighteen',
	 'nineteen']

ll = {2: 'twenty', 3: 'thirty',
	  4: 'forty', 5: 'fifty',
	  6: 'sixty', 7: 'seventy',
	  8: 'eighty', 9: 'ninety'}

def numToWords(n):
	if n < 20:
		return l[n]
	elif n % 10 == 0:
		return ll[n//10]
	else:
		return str(ll[n//10]) + "-" + str(l[n%10])

while True:
	try:
		line = input().split()
	except EOFError:
		break

	op = list()
	for i in range(len(line)):
		if i == 0 and line[i].isdigit():
			op.append(numToWords(int(line[0])).capitalize())
		elif line[i].isdigit():
			op.append(numToWords(int(line[i])))
		else:
			op.append(line[i])
	print(" ".join(op))
