d = dict()
l = ['clank', 'bong', 'click', 'tap', 'poing', 'clonk', 'clack', 'ping', 'tip', 'cloing', 'tic', 'cling', 'bing', 'pong', 'clang', 'pang', 'clong', 'tac', 'boing', 'boink', 'cloink', 'rattle', 'clock', 'toc', 'clink', 'tuc']
for i in range(ord('A'), ord('Z')+1):
	d[l[i-ord('A')]] = chr(i)
d['whack'] = ' '

capslock = 0
shift = 0

l = list()

N = int(input())
for i in range(N):
	sound = input()
	if sound == 'pop':
		if len(l) > 0:
			l.pop()
		continue
	elif sound == 'dink':
		shift = 1
		continue
	elif sound == 'thumb':
		shift = 0
		continue
	elif sound == 'bump':
		capslock = 0 if capslock == 1 else 1
		continue

	if capslock + shift == 1:
		l.append(d[sound].upper())
	else:
		l.append(d[sound].lower())
print("".join(l))