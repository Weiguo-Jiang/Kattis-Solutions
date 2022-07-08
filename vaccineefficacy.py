N = int(input())
cont = 0
vac = 0
contA = 0
vacA = 0
contB = 0
vacB = 0
contC = 0
vacC = 0
for i in range(N):
	l = [i for i in input()]
	if l[0] == 'N':
		cont += 1
		if l[1] == 'Y':
			contA += 1
		if l[2] == 'Y':
			contB += 1
		if l[3] == 'Y':
			contC += 1
	else:
		vac += 1
		if l[1] == 'Y':
			vacA += 1
		if l[2] == 'Y':
			vacB += 1
		if l[3] == 'Y':
			vacC += 1
if contA/cont > vacA/vac:
	print((contA/cont-vacA/vac)/(contA/cont)*100)
else:
	print("Not Effective")

if contB/cont > vacB/vac:
	print((contB/cont-vacB/vac)/(contB/cont)*100)
else:
	print("Not Effective")

if contC/cont > vacC/vac:
	print((contC/cont-vacC/vac)/(contC/cont)*100)
else:
	print("Not Effective")