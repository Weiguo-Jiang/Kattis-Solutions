n = int(input())

l = list()
for i in range(n):
    inp = input().split()
    l.append(int(inp[1]))

l.sort(reverse=True)

s = 0
for i in range(0, n, 2):
    s += l[i]

print(s)