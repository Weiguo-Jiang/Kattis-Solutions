n = int(input())
Dutch = input().split()
m = int(input())
dic = dict()
for i in range(m):
	d, e, c = input().split()
	if d in dic:
		dic[d].append([e, c])
	else:
		dic[d] = list()
		dic[d].append([e, c])

comb = 1
correct = 1
for i in Dutch:
	cnt = 0
	for j in dic[i]:
		if j[1] == 'correct':
			cnt += 1
	correct *= cnt
	comb *= len(dic[i])
incorrect = comb-correct

if comb == 1:
	l = list()
	for i in Dutch:
		l.append(dic[i][0][0])
	print(" ".join(l))
	if incorrect == 1:
		print("incorrect")
	else:
		print("correct")
else:
	print(str(correct) + " correct")
	print(str(incorrect) + " incorrect")
