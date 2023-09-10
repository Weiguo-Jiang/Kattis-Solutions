N, K = map(int, input().split())
for i in range(N):
    x = int(input())
    while x%2 == 0:
        x //= 2
        K -= 1

print(0 if K > 0 else 1)