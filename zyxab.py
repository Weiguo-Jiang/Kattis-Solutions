n = int(input())
minLen = 21
l = list()
for i in range(n):
	word = input()
	s = set([i for i in word])
	if len(s) < len(word):
		continue
	if len(word) < 5:
		continue
	if len(word) < minLen:
		minLen = len(word)
	l.append(word)

l = sorted([i for i in l if len(i) == minLen])
if len(l) == 0:
	print("neibb!")
else:
	print(l[-1])