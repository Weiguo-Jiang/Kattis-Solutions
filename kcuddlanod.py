N, M = input().split()
N = int("".join(reversed(['5' if N[i] == '2' else ('2' if N[i] == '5' else N[i]) for i in range(len(N))])))
M = int("".join(reversed(['5' if M[i] == '2' else ('2' if M[i] == '5' else M[i]) for i in range(len(M))])))
print(1 if N > M else 2)