R, B = list(map(int, input().split()))
product = R+B

factor = list()
for i in range(2, int(product**0.5)+1):
	if product % i == 0:
		factor.append(i)

for i in factor:
	if ((i-2)*(product//i-2) == B) and (2*i+2*(product//i)-4 == R):
		print(str(product//i)+" "+str(i))
		break