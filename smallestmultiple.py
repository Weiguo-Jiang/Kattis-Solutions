from math import ceil

def isPrime(n):
    for i in range(2, ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def breakDown(n):
    d = dict()
    if n == 1:
        d[1] = 1
        return d
    while n != 1:
        if isPrime(n):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            break
        for i in range(2, ceil(n**0.5)+1):
            if n%i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                n //= i
                break
    return d


while True:
    try:
        inp = list(map(int, input().split()))
    except EOFError:
        break

    l = list()
    for i in inp:
        l.append(breakDown(i))
    
    d = l[0]
    for i in range(1, len(l)):
        dd = l[i]
        for key, value in dd.items():
            if key in d and value > d[key]:
                d[key] = value
            elif key not in d:
                d[key] = value
    ans = 1
    for key, value in d.items():
        ans *= (key**value)
    print(ans)