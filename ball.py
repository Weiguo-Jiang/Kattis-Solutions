n = int(input())
s = set()
for i in range(n//2+1):
    a, b = map(int, input().split())
    if (a in s) or (b in s):
        print('{0} {1}'.format(min(a, b), max(a, b)))
        break
    s.add(a)
    s.add(b)