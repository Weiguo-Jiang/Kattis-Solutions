words = list()
while True:
	try:
		wl = input().split()
	except EOFError:
		break
	for i in wl:
		words.append(i)

s = set()
for i in words:
	for j in words:
		if i != j:
			s.add(i+j)
for i in sorted(list(s)):
	print(i)
