def binaryMinSearch(l, u, n):
	while l < u:
		m = (l+u)//2
		if nums[m] > n:
			u = m
		else:
			l = m+1

	if nums[l] > n:
		return l - 1
	else:
		return l


def binaryMaxSearch(l, u, n):
	while l < u:
		m = (l+u)//2
		if nums[m] >= n:
			u = m
		else:
			l = m+1

	if nums[l] < n:
		return l+1
	else:
		return l


N = int(input())
nums = sorted(list(map(int, input().split())))
maximum = nums[-1]
minimum = nums[0]
Q = int(input())
for i in range(Q):
	l, r = list(map(int, input().split()))
	if l <= minimum and r >= maximum:
		print(N)
	elif l > maximum and r > maximum:
		print(0)
	elif l < minimum and r < minimum:
		print(0)
	elif l <= minimum:
		index = binaryMinSearch(0, N-1, r)
		print(index+1)
	elif r >= maximum:
		index = binaryMaxSearch(0, N-1, l)
		print(N-index)
	else:
		index1 = binaryMaxSearch(0, N-1, l)
		index2 = binaryMinSearch(0, N-1, r)
		print(index2-index1+1)