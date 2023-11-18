N = int(input())
l=[]
l.append('+'+'-'*N+'+')
for _ in range(N):
    l.append('|'+' '*(N)+'|')
l.append('+'+'-'*N+'+')
for i in l:
    print(i)
