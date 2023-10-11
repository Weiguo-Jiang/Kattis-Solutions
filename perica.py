from math import comb

N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

cnt = 0
for i in range(K-1, N):
    cnt += l[i]*comb(i, K-1)
    cnt %= 1000000007
print(cnt)
