import math

N, K = list(map(int, input().split()))
angles = list(map(int, input().split()))
n = 360
for i in angles:
	n = math.gcd(n, i)

given = list(map(int, input().split()))
for i in given:
	if i%n == 0:
		print("YES")
	else:
		print("NO")