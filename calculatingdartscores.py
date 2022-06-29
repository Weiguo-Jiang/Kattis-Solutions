n = int(input())
if n == 1:
	print("single 1")
elif n == 2:
	print("double 1")
else:
	l = list()
	ll = list()
	for i in range(1, 21):
		l.append(i)
		l.append(2*i)
		l.append(3*i)

		ll.append("single " + str(i))
		ll.append("double " + str(i))
		ll.append("triple " + str(i))

	flag = 0
	for i in range(len(l)):
		for j in range(len(l)):
			for k in range(len(l)):
				if l[i] + l[j] + l[k] == n:
					print(ll[i])
					print(ll[j])
					print(ll[k])
					flag = 1
					break
			if flag:
				break
		if flag:
			break

	if not flag:
		print("impossible")