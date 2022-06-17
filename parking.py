A, B, C = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))
d = dict()
for i in range(t1, t2):
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

t3, t4 = list(map(int, input().split()))
for i in range(t3, t4):
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

t5, t6 = list(map(int, input().split()))
for i in range(t5, t6):
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

price = 0
for key, value in d.items():
	if value == 3:
		price += 3*C
	elif value == 2:
		price += 2*B
	else:
		price += A
print(price)