b, k, g = list(map(int, input().split()))
groups = k // g
b -= 1
mod = b % groups
if mod == 0:
	print(b//groups)
else:
	print(b//groups+1)