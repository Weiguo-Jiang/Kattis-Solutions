T = int(input())
for i in range(T):
	a, b = list(map(int, input().split()))
	root1 = (4*(a+b)+(16*(a+b)**2-48*a*b)**0.5)/24
	root2 = (4*(a+b)-(16*(a+b)**2-48*a*b)**0.5)/24
	volume1 = (a-2*root1)*(b-2*root1)*root1
	volume2 = (a-2*root2)*(b-2*root2)*root2
	print(max(volume1, volume2))