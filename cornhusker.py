l = list(map(int, input().split()))
total = 0
for i in range(0, len(l), 2):
    A, L = l[i], l[i+1]
    total += A * L
total //= 5
N, KWF = map(int, input().split())
print(int(total*N/KWF))