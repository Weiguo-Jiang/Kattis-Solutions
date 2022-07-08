case = 1
while True:
	try:
		n = int(input())
	except EOFError:
		break

	nums = list()
	sums = list()
	for i in range(n):
		num = int(input())
		nums.append(num)
	for i in range(n-1):
		for j in range(i+1, n):
			sums.append(nums[i]+nums[j])

	print("Case " + str(case) + ":")
	case += 1
	m = int(input())
	for i in range(m):
		closest = 100000001
		closestSum = 0
		q = int(input())
		for j in sums:
			if abs(q-j) < closest:
				closest = abs(q-j)
				closestSum = j
		print("Closest sum to " + str(q) + " is " + str(closestSum) + ".")	

