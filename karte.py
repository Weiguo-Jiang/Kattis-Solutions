s = input()
flag = 0
d = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
for i in range(0, len(s)-2, 3):
	l = len(d[s[i]])
	d[s[i]].add(s[i+1:i+3])
	l1 = len(d[s[i]])
	if l == l1:
		flag = 1
if flag:
	print("GRESKA")
else:
	lst = list()
	for key, value in d.items():
		lst.append(str(13-len(value)))
	print(" ".join(lst))