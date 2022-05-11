n = int(input())
l = list(map(int, input().split()))
cnt = 0
s = 0
for i in l:
	if i != -1:
		cnt += 1
		s += i
print(s/cnt)