score = 0
n = 0
for i in range(5):
	s = sum(list(map(int, input().split())))
	if s > score:
		score = s
		n = i+1
print(str(n) + " " + str(score))
