from math import gcd

def recur(m, n):
    div = gcd(m, n)
    return int(m%2==1 and n%2==1) if div == 1 else div*recur(m//div, n//div)

m, n = map(int, input().split())
print(recur(m, n))