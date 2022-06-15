n, k = list(map(int, input().split()))
d, s = list(map(int, input().split()))
avg = (n*d-k*s)/(n-k)
if avg > 100 or avg < 0:
	print("impossible")
else:
	print(avg)