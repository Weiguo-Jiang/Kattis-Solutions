n = int(input())
l = list(map(int, input().split()))

minList = [2**32 for i in range(n)]
for i in range(n-2, -1, -1):
	minList[i] = minList[i+1]
	if l[i+1] < minList[i]:
		minList[i] = l[i+1]

cnt = 0
maximum = -2**32
for i in range(n):
	if l[i] > maximum and l[i] < minList[i]:
		cnt += 1
	if l[i] > maximum:
		maximum = l[i]
print(cnt)