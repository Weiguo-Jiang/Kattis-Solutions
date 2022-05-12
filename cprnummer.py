s = input()
l = list()
for i in s:
	if i != '-':
		l.append(int(i))
print(int((4*l[0]+3*l[1]+2*l[2]+7*l[3]+6*l[4]+5*l[5]+4*l[6]+3*l[7]+2*l[8]+l[9])%11 == 0))