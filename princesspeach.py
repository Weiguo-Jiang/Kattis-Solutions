N, Y = list(map(int, input().split()))
s = set()
for i in range(Y):
	s.add(int(input()))
for i in range(N):
	if i not in s:
		print(i)
print("Mario got " + str(len(s)) + ' of the dangerous obstacles.')