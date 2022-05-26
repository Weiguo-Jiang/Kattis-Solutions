l = sorted(list(map(int, input().split())))
gap1 = l[1]-l[0]
gap2 = l[2]-l[1]
if gap1 == gap2*2:
	print(l[0]+gap2)
elif gap2 == gap1*2:
	print(l[1]+gap1)
else:
	print(l[2]+gap1)
