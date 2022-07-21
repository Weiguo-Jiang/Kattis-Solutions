N, t = list(map(int, input().split()))
arr = list(map(int, input().split()))
if t == 1:
	print(7)
elif t == 2:
	if arr[0] > arr[1]:
		print("Bigger")
	elif arr[0] == arr[1]:
		print("Equal")
	else:
		print("Smaller")
elif t == 3:
	print(sorted(arr[0:3])[1])
elif t == 4:
	print(sum(arr))
elif t == 5:
	s = 0
	for i in arr:
		if i % 2 == 0:
			s += i
	print(s)
elif t == 6:
	l = list()
	for i in arr:
		l.append(chr(i%26+97))
	print("".join(l))
elif t == 7:
	s = set()
	flag = 0
	i = 0
	s.add(0)
	while True:
		i = arr[i]
		if i > N-1:
			print("Out")
			break
		elif i == N-1:
			print("Done")
			break
		if i in s:
			flag = 1
			break
		else:
			s.add(i)
	if flag:
		print("Cyclic")