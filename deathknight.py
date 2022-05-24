n = int(input())
cnt = n
for i in range(n):
	l = input()
	for j in range(len(l)-1):
		if l[j] == 'C' and l[j+1] == 'D':
			cnt -= 1
			break
print(cnt)