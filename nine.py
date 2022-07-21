T = int(input())
for i in range(T):
	d = int(input())
	ans = 8*pow(9, d-1, 1000000007)
	print(ans%1000000007)