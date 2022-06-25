n, p, m = list(map(int, input().split()))
d = dict()
for i in range(n):
	d[input()] = 0

maximum = -1
for i in range(m):
	inp = input().split()
	d[inp[0]] += int(inp[1])
	if d[inp[0]] > maximum:
		maximum = d[inp[0]]

if maximum < p:
	print("No winner!")
else:
	for key, value in d.items():
		if value >= p:
			print(key + " wins!")