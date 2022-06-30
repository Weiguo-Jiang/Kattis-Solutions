h, P = list(map(int, input().split()))
days = 0
bulbCnt = 1
bulbCost = 5
lampCost = 60
while bulbCost <= lampCost:
	days += 1
	if days*h > bulbCnt*1000:
		bulbCnt += 1
		bulbCost += 5

	bulbDaily = 60*h*P/100000
	lampDaily = 11*h*P/100000

	bulbCost += bulbDaily
	lampCost += lampDaily

print(days)
