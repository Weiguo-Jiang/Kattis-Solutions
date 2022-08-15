T = int(input())
for i in range(1, T+1):
	print("Recipe # " + str(i))
	R, P, D = list(map(int, input().split()))
	ratio = D / P

	d = dict()
	main = 0
	for j in range(R):
		inp = input().split()
		name, weight, percentage = inp[0], float(inp[1]), float(inp[2])
		d[name] = percentage
		if percentage == 100.0:
			main = weight*ratio

	scaled = dict()
	for key, value in d.items():
		scaled[key] = main*value/100.0

	for key, value in scaled.items():
		print(key + " " + str(round(value, 1)))

	print('-'*40)
