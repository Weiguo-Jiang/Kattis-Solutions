N = int(input())
time = -1
pub = ''
for _ in range(N):
    p, k, t = input().split()
    k, t = int(k), int(t)
    if (k+1)*t > time:
        time = (k+1)*t
        pub = p
print(pub, time)