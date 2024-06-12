n = int(input())
bestName = ''
bestScore = -1
for i in range(n):
    name, score = input().split()
    score = int(score)
    if score > bestScore:
        bestName = name
        bestScore = score

print(bestName)
