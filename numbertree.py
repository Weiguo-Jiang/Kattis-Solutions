inp = input()
if inp[-1] == ' ':
	H = int(inp.split()[0])
	print(2**(H+1)-1)
else:
	H, s = inp.split()
	H = int(H)
	n = 2**(H+1)-1
	pos = 0
	for i in s:
		if i == 'L':
			pos = pos*2 + 1
		else:
			pos = 2 * (pos+1)
	print(n-pos)