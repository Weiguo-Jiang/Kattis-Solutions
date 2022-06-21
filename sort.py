import operator

N, C = list(map(int, input().split()))
freqD = dict()
posD = dict()

numbers = list(map(int, input().split()))
for i in range(len(numbers)):
	if numbers[i] not in freqD:
		freqD[numbers[i]] = 1
	else:
		freqD[numbers[i]] += 1

	if numbers[i] not in posD:
		posD[numbers[i]] = i

freqD = dict(sorted(freqD.items(), key=operator.itemgetter(1), reverse=True))

s = set()
for key, value in freqD.items():
	if value not in s:
		s.add(value)

l = sorted(list(s))
l.reverse()

op = list()

for i in l:
	ll = list()
	for key, value in freqD.items():
		if value == i:
			ll.append(key)
	if len(ll) > 1:
		for j in range(len(ll)):
			for k in range(len(ll)-j-1):
				if posD[ll[k]] > posD[ll[k+1]]:
					c = posD[ll[k]]
					posD[ll[k]] = posD[ll[k+1]]
					posD[ll[k+1]] = c
	
	for j in ll:
		lll = list()
		for k in range(i):
			lll.append(str(j))
		op.append(" ".join(lll))

print(" ".join(op))