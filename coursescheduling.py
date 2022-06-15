n = int(input())
s = set()
for i in range(n):
	s.add(input())
l = list(s)

courses = list()
d = dict()
for i in l:
	course = i.split()[-1]
	if course not in d:
		d[course] = 1
	else:
		d[course] += 1
for key in d:
	courses.append(key)
courses = sorted(courses)

for i in courses:
	print(i, end=" ")
	print(d[i])