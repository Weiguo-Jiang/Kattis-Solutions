T = int(input())
for i in range(T):
    S = int(input())
    d = dict()
    adj = dict()
    for j in range(S):
        inp = input().split()
        if len(inp) == 2:
            if inp[1] == 'favourably':
                d[inp[0]] = 1
            else:
                d[inp[0]] = 0
        else:
            adj[inp[0]] = inp[1:]

    def recur(node):
        if node in d:
            return d[node]
        else:
            ans = 0
            for i in adj[node]:
                ans += recur(i)
            d[node] = ans
            return ans

    print(recur('1'))