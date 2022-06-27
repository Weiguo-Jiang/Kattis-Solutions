t1 = list(map(int, input().split(":")))
t2 = list(map(int, input().split(":")))

t1 = t1[0]*60*60+t1[1]*60+t1[2]
t2 = t2[0]*60*60+t2[1]*60+t2[2]

if t1 < t2:
	d = t2-t1
	h = d//3600
	d %= 3600
	m = d//60
	d %= 60
	s = d

	if h < 10:
		h = '0'+str(h)
	if m < 10:
		m = '0'+str(m)
	if s < 10:
		s = '0'+str(s)

	print(str(h)+":"+str(m)+":"+str(s))

elif t1 == t2:
	print("24:00:00")

else:
	d = 24*60*60-(t1-t2)
	h = d//3600
	d %= 3600
	m = d//60
	d %= 60
	s = d
	if h < 10:
		h = '0'+str(h)
	if m < 10:
		m = '0'+str(m)
	if s < 10:
		s = '0'+str(s)

	print(str(h)+":"+str(m)+":"+str(s))