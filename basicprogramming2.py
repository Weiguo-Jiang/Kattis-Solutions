N, t = list(map(int, input().split()))
arr = list(map(int, input().split()))

if t == 1:
	flag = 1
	s = set(arr)
	for i in arr:
		if 7777-i in s:
			print("Yes")
			flag = 0
			break
	if flag:
		print("No")

elif t == 2:
	s = set(arr)
	if len(s) < N:
		print("Contains duplicate")
	else:
		print("Unique")
elif t == 3:
	flag = 1
	d = dict()
	for i in arr:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	for key, value in d.items():
		if value > N/2:
			print(key)
			flag = 0
			break
	if flag:
		print(-1)
elif t == 4:
	l = sorted(arr)
	if N % 2 == 1:
		print(l[N//2])
	else:
		print(str(l[N//2-1])+" "+str(l[N//2]))
elif t == 5:
	l = sorted(arr)
	ll = list()
	for i in l:
		if i >= 100 and i <= 999:
			ll.append(str(i))
	print(" ".join(ll))