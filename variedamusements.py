n, a, b, c = map(int, input().split())

mod = 1000000007

d = dict()
def recur(depth, type):
    if depth == 0:
        return 1

    if (depth, type) in d:
        return d[(depth, type)]

    if type == 'a':
        ans = b*recur(depth-1, 'b') + c*recur(depth-1, 'c')
    elif type == 'b':
        ans = a*recur(depth-1, 'a') + c*recur(depth-1, 'c')
    elif type == 'c':
        ans = a*recur(depth-1, 'a') + b*recur(depth-1, 'b')

    d[(depth, type)] = ans % mod

    return ans % mod

print((a*recur(n-1, 'a') + b*recur(n-1, 'b') + c*recur(n-1, 'c')) % mod)
