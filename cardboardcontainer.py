V = int(input())
l = list()

for i in range(1, int(V**0.5)+1):
	if V%i == 0:
		for j in range(1, int(V//i**0.5)+1):
			if (V//i)%j == 0:
				l.append([i, j, V//i//j])

cheapest = 1e18
for i in l:
	l, w, h = i
	cost = 2*(l*w+w*h+l*h)
	if cost < cheapest:
		cheapest = cost
print(cheapest)