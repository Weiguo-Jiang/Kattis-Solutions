N, B = input().split()
N = int(N)
dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
indominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
points = 0
for i in range(4*N):
	s = input()
	if s[1] == B:
		points += dominant[s[0]]
	else:
		points += indominant[s[0]]
print(points)