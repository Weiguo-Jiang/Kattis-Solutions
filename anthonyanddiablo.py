import math
A, N = list(map(float, input().split()))
maxArea = (N/2/math.pi)**2*math.pi
if maxArea > A:
	print("Diablo is happy!")
else:
	print("Need more materials!")