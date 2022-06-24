C = int(input())
for i in range(C):
	inp = list(map(int, input().split()))
	avg = sum(inp[1:])/inp[0]
	cnt = 0
	for j in range(1, inp[0]+1):
		if inp[j] > avg:
			cnt += 1
	
	percentage = str(round(cnt*100/inp[0], 3))
	l = [i for i in percentage]
	index = 0
	for j in range(len(l)):
		if l[j] == '.':
			index = j
	if len(l[index+1:]) < 3:
		for j in range(3-len(l[index+1:])):
			l.append('0')
	l.append('%')
	print("".join(l))