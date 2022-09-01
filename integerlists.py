from collections import deque

t = int(input())
for i in range(t):
	p = input()
	n = int(input())
	l = input()
	if n == 0 and 'D' in p:
		print("error")
		continue
	elif n == 0 and 'D' not in p:
		print('[]')
		continue
	else:
		l = [int(i) for i in l[1:len(l)-1].split(',')]
		q = deque()
		for i in l:
			q.append(i)
		flag = 0
		error = 0
		for c in p:
			if c == 'R':
				flag = 1-flag
			else:
				if len(q) == 0:
					print("error")
					error = 1
					break
				if flag == 0:
					q.popleft()
				else:
					q.pop()
		if error:
			continue
		
		l = [str(i) for i in q]
		if flag:
			l.reverse()
			print('[', end="")
			print(",".join(l), end=']\n')
		else:
			print('[', end="")
			print(",".join(l), end=']\n')
