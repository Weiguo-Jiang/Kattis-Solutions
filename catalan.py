import math
import operator as op
from functools import reduce
nCr = lambda n, r: reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
catalan = lambda n: nCr(2 * n, n) // (n + 1)
q = int(input())
for _ in range(q):
    print(catalan(int(input())))