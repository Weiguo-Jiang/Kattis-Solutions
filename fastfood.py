t = int(input())
for i in range(t):
	n, m = list(map(int, input().split()))
	prizes = list()
	dicts = list()
	for j in range(n):
		d = dict()
		inp = list(map(int, input().split()))
		prizes.append(inp[-1])
		for k in range(1, len(inp)-1):
			if inp[k] not in d:
				d[inp[k]] = 1
			else:
				d[inp[k]] += 1
		dicts.append(d)
	d = dict()
	tickets = list(map(int, input().split()))
	for j in range(1, len(tickets)+1):
		d[j] = tickets[j-1]

	cash = 0	
	for j in range(len(dicts)):
		m = 101
		for key in dicts[j]:
			cnt = d[key] // dicts[j][key]
			if cnt < m:
				m = cnt
		cash += m*prizes[j]
	print(cash)
