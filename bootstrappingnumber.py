n = int(input())
approx = 1
high = 10
low = 1
for i in range(1000):
	p = approx**approx
	if p == n:
		break
	elif p < n:
		low = approx
		approx = (approx+high)/2
	elif p > n:
		high = approx
		approx = (approx+low)/2
print(approx)
