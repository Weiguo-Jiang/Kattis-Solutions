f = open('test.txt', 'w')
for i in range(1, 20001):
	f.write(str(i*10000)+'\n')
f.close()