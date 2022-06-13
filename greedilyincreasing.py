N = int(input())
inp = list(map(int, input().split()))
l = list()
currMax = -1
for i in inp:
	if i > currMax:
		l.append(str(i))
		currMax = i
print(len(l))
print(" ".join(l))