n = int(input())
d1 = dict()
d2 = dict()
d3 = dict()
l = list()
for i in range(n):
	inp = input().split()
	name, firstLeg, otherLegs = inp[0], float(inp[1]), float(inp[2])
	d1[name] = firstLeg

	if otherLegs in d2:
		d2[otherLegs].add(name)
	else:
		d2[otherLegs] = set()
		d2[otherLegs].add(name)

	d3[name] = otherLegs

	l.append(otherLegs)

l.sort()

minTime = 2**32
names = list()
for name, time in d1.items():
	ll = l.copy()
	ll.remove(d3[name])

	time = d1[name] + sum(ll[0:3])
	team = set()
	for i in ll[0:3]:
		for key, value in d3.items():
			if value == i and key not in team and key != name:
				team.add(key)
				break

	if time < minTime:
		names = [name] + list(team)
		minTime = time

print(minTime)
for i in names:
	print(i)
