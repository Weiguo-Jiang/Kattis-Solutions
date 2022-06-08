n = int(input())
l = list()
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = list()
for i in range(97, 123):
	if chr(i) not in vowels:
		consonants.append(chr(i))

ll = list()
for a in consonants:
	ll.append(a)
	for b in vowels:
		ll.append(b)
		for c in consonants:
			ll.append(c)
			for d in vowels:
				ll.append(d)
				for e in consonants:
					ll.append(e)
					l.append("".join(ll))
					ll.pop()
				ll.pop()
			ll.pop()
		ll.pop()
	ll.pop()

for i in range(n):
	print(l[i])