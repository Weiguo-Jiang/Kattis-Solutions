n, h, v = list(map(int, input().split()))
h1 = n-h
v1 = n-v
print(4*max(h*v, h*v1, h1*v1, v*h1))