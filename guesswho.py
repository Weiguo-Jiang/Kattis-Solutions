N, M, Q = map(int, input().split())
characters = []
for _ in range(N):
    characters.append(input())
cnt = 0
unique = ''
queries = []
for _ in range(Q):
    A, M = input().split()
    queries.append((int(A)-1, M))
for character in characters:
    flag = True
    for query in queries:
        if character[query[0]] != query[1]:
            flag = False
            break
    if flag:
        unique = characters.index(character)
        cnt += 1

if cnt == 1:
    print("unique")
    print(unique+1)
else:
    print("ambiguous")
    print(cnt)
