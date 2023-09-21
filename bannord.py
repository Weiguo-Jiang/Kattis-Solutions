f = [i for i in input()]
l = input().split()

for i in range(len(l)):
    for j in l[i]:
        if j in f:
            l[i] = "*"*len(l[i])

print(" ".join(l))