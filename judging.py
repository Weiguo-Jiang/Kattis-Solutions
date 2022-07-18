n = int(input())
DOM = dict()
Kattis = dict()
for i in range(n):
	judge = input()
	if judge in DOM:
		DOM[judge] += 1
	else:
		DOM[judge] = 1
for i in range(n):
	judge = input()
	if judge in Kattis:
		Kattis[judge] += 1
	else:
		Kattis[judge] = 1

cnt = 0
for key, value in DOM.items():
	if key in Kattis:
		cnt += min(value, Kattis[key])
print(cnt)