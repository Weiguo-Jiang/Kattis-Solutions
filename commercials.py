N, P = list(map(int, input().split()))
inp = [int(i)-P for i in input().split()]

curSum = 0
maxSum = 0
for i in inp:
	curSum += i
	if curSum > maxSum:
		maxSum = curSum

	if curSum < 0:
		curSum = 0

print(maxSum)