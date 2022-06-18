n = int(input())
inp = sorted(list(map(int, input().split())))
s = 0
v = -1
for i in range(n):
	if inp[i] != v+1:
		s += inp[i]
		v = inp[i]
	else:
		v += 1
print(s)