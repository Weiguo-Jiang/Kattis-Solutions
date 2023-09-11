N = int(input())
A = list(map(int, input().split()))

d = dict()
for i in range(1, 7):
    for j in range(1, 7):
        s = i+j
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

cnt = 0
for i in range(N):
    cnt += d[A[i]]

print(cnt/36)