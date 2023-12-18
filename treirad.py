N = int(input())
cnt = 0
for i in range(1, N):
    if i*(i+1)*(i+2) >= N:
        break
    elif i*(i+1)*(i+2) < N:
        cnt += 1
print(cnt)