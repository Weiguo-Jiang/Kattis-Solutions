k, r = list(map(int, input().split()))
ingredients = list(map(int, input().split()))
revenue = 0
for i in range(r):
	l = list(map(int, input().split()))
	p = l[-1]
	l.pop()

	n = 2**32
	for j in range(k):
		if l[j] != 0 and ingredients[j] // l[j] < n:
			n = ingredients[j] // l[j]
	if n*p > revenue:
		revenue = n*p
print(revenue)