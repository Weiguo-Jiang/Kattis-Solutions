N = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
party = 0
for i in range(0, N):
	if l[i] + i + 1 > party:
		party = l[i] + i + 1
print(party+1)