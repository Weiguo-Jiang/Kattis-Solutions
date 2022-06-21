from itertools import chain, combinations

def powerSet(l):
	return chain.from_iterable(combinations(l, r) for r in range(len(l)+1))

N = int(input())
l = list()
for i in range(N):
	taste = list(map(int, input().split()))
	l.append(taste)

l = list(powerSet(l))
l = [i for i in l if len(i) > 0]
smallest = 1000000000
for i in l:
	sourness = 1
	bitterness = 0
	if len(i) > 0:
		for j in i:
			sourness *= j[0]
			bitterness += j[1]
	if abs(sourness-bitterness) < smallest:
		smallest = abs(sourness-bitterness)
print(smallest)