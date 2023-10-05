n, c, p = map(int, input().split())
cnt = 0
for i in range(n):
    jump = int(input())
    if jump > c+p:
        cnt += 1
        p = c
        c = jump
print(cnt)