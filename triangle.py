import math
case = 1
while True:
	try:
		n = int(input())
	except EOFError:
		break
	print("Case " + str(case) + ": ", end="")
	c = 1 + int((n+1)*math.log10(3)-n*math.log10(2))
	print(c)
	case += 1
