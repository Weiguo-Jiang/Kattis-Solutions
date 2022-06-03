cnt = 1
while True:
	d = dict()
	n = int(input())
	if n == 0:
		break
	for i in range(n):
		inp = input().split()
		animal = inp[-1].lower()
		if animal in d:
			d[animal] += 1
		else:
			d[animal] = 1
	print("List " + str(cnt) + ":")
	cnt += 1

	for key, value in sorted(d.items()):
		print(key + " | " + str(value)) 