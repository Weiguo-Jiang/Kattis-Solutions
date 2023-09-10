n = int(input())
l = [int(x) for x in input()]
l += [0, 0]
ll = [i for i in l]

for i in range(n):
    if l[i] == 1:
        ll[i+1] = 1
        ll[i+2] = 1

print(sum(ll[:n]))