l = list()
word = [i for i in input()]
for i in range(1, len(word)-1):
	for j in range(i, len(word)-1):
		w1 = [word[c] for c in range(i)]
		w2 = [word[c] for c in range(i, j+1)]
		w3 = [word[c] for c in range(j+1, len(word))]
		w1.reverse()
		w2.reverse()
		w3.reverse()
		l.append("".join(w1)+"".join(w2)+"".join(w3))
l.sort()
print(l[0])