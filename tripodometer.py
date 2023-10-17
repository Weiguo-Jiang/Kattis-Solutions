N = int(input())
l = list(map(int, input().split()))
s = sum(l)
d = set()
for i in range(N):
    d.add(s-l[i])
print(len(d))
print(" ".join(map(str, sorted(d))))