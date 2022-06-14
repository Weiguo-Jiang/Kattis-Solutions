l = list()
while True:
	r, c = list(map(int, input().split()))
	if r == 0 and c == 0:
		break
	ll = list()
	for i in range(r):
		ll.append([c for c in input()])
	lll = list()
	for i in range(c):
		llll = list()
		for j in range(r):
			llll.append(ll[j][i])
		lll.append(llll)

	for i in range(c):
		for j in range(c-i-1):
			if "".join(lll[j]).lower() > "".join(lll[j+1]).lower():
				cp = lll[j]
				lll[j] = lll[j+1]
				lll[j+1] = cp
	
	for i in range(r):
		ll = list()
		for j in range(c):
			ll.append(lll[j][i])
		l.append("".join(ll))
	l.append('\n')

for i in range(len(l)-1):
	if l[i] == '\n':
		print()
	else:
		print(l[i])