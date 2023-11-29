N = int(input())
cnt = 0
for _ in range(N):
    g, b = map(int, input().split())
    cnt += g
    if cnt < b:
        print("impossible")
        exit()
print("possible")