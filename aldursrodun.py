import itertools
from math import gcd

n = int(input())
l = map(int, input().split())

candidates = list(itertools.permutations(l))

flag = 1
for c in candidates:
    if all(gcd(c[i], c[i+1]) > 1 for i in range(n-1)):
        print(' '.join(map(str, c)))
        flag = 0
        break
if flag:
    print("Neibb")