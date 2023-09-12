n, k, d = map(int, input().split())

cnt = 0
for i in range(n):
    f = int(input())

    if f + 14 <= d + k:
        cnt += 1

print(cnt)