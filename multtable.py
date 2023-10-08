from math import sqrt, ceil

N, M = map(int, input().split())

cnt = 0
for i in range(1, min(N, ceil(sqrt(M)))+1):
    if M%i == 0 and M//i <= N:
        cnt += 2 if i*i != M else 1
print(cnt)
