import math

inp = input()
index = 0
for i in range(len(inp)):
	if inp[i] == '/':
		index = i
		break

numerator = int(inp[:index])
denominator = int(inp[index+1:])

numerator -= denominator * 32
numerator *= 5
denominator *= 9
gcd = math.gcd(numerator, denominator)
if numerator == 0:
	print("0/1")
else:
	print(str(numerator//gcd) + "/" + str(denominator//gcd))