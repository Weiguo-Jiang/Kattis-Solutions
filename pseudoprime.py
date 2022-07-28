from math import ceil

def isComposite(n):
	for i in range(2, ceil(n**0.5)+1):
		if n%i == 0:
			return True
	return False


while True:
	p, a = list(map(int, input().split()))
	if p == 0 and a == 0:
		break

	if isComposite(p) and pow(a, p, p) == a:
		print("yes")
	else:
		print("no")