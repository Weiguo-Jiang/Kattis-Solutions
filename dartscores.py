def score(rSquare):
	if rSquare <= 400:
		return 10
	elif rSquare <= 1600:
		return 9
	elif rSquare <= 3600:
		return 8
	elif rSquare <= 6400:
		return 7
	elif rSquare <= 10000:
		return 6
	elif rSquare <= 14400:
		return 5
	elif rSquare <= 19600:
		return 4
	elif rSquare <= 25600:
		return 3
	elif rSquare <= 32400:
		return 2
	elif rSquare <= 40000:
		return 1
	else:
		return 0


T = int(input())
for i in range(T):
	totalScore = 0
	n = int(input())
	for j in range(n):
		x, y = list(map(int, input().split()))
		rSquare = x**2+y**2
		totalScore += score(rSquare)
	print(totalScore)