N, M = map(int, input().split())

l = []
for i in range(N):
    l.append(list(map(int, input().split())))

for i in range(1, M):
    l[0][i] += l[0][i-1]

for i in range(1, N):
    l[i][0] += l[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        l[i][j] += max(l[i-1][j], l[i][j-1])

ans = []
for i in range(N):
    ans.append(str(l[i][M-1]))
print(" ".join(ans))