inp = input().split()
l = list()
for i in inp:
	flag = 1
	ll = list()
	for c in i:
		asi = ord(c)
		if c == 'u' or c == 'm':
			ll.append(c)
		elif (asi >= 48 and asi <= 57) or (asi >= 65 and asi <= 90) or (asi >= 97 and asi <= 122):
			flag = 0
			break
	if flag:
		for j in ll:
			l.append(j)

ans = list()
for i in range(0, len(l)-6, 7):
	um = l[i:i+7]
	pw = 0
	deci = 0
	for j in range(len(um)-1, -1, -1):
		if um[j] == 'u':
			deci += (1 << pw)
		pw += 1
	ans.append(chr(deci))

print("".join(ans))