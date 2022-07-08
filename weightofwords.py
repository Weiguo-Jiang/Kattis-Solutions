l, w = list(map(int, input().split()))
if w < l or w > 26*l:
	print("impossible")
else:
	ll = ['a' for i in range(l)]
	weight = l
	for i in range(w-l):
		index = i%l
		ll[index] = chr(ord(ll[index])+1)
	print("".join(ll))