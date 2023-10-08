N = int(input())
stairs = list(map(int, input().split()))
stairs.append(0)
effort = 0
for i in range(N):
    effort += max((stairs[i] - stairs[i+1] - 1), 0)
print(effort)