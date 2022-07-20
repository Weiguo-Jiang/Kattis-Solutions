N = int(input())
cnt = 0
for i in range(N):
	if input() == 'O':
		cnt += 2**(N-i-1)
print(cnt)