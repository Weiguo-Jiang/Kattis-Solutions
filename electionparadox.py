N = int(input())
l = sorted(list(map(int, input().split())))
l.reverse()
n = 0
for i in range(N//2):
	n += l[i]

for i in range(N//2, N):
	n += l[i]//2
print(n)
