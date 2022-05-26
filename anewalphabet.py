d = dict()
l = ['@', '8', '(', '|)', '3', '#', '6', '[-]',
	 '|', '_|', '|<', '1', '[]\\/[]', '[]\\[]',
	 '0', '|D', '(,)', '|Z', '$', '\'][\'', '|_|',
	 '\\/', '\\/\\/', '}{', '`/', '2']
for i in range(26):
	d[chr(ord('a')+i)] = l[i]

l = input().lower()
for i in l:
	if i in d:
		print(d[i], end="")
	else:
		print(i, end="")
print()
