X, Y = list(map(int, input().split()))
if X == 0 and Y == 1:
	print("ALL GOOD")
elif Y == 1:
	print("IMPOSSIBLE")
else:
	print(X/(1-Y))