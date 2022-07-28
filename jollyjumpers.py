while True:
	try:
		l = list(map(int, input().split()))
	except EOFError:
		break

	if l[0] == 1:
		print("Jolly")
	else:
		s = set()
		for i in range(1, len(l)-1):
			s.add(abs(l[i]-l[i+1]))
		
		flag = 1
		for i in range(1, l[0]):
			if i not in s:
				flag = 0
				print("Not jolly")
				break
		if flag:
			print("Jolly")