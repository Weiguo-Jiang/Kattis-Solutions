from math import ceil, sqrt

N = int(input())
for _ in range(N):
    msg = [c for c in input()]
    sq = (ceil(sqrt(len(msg))))**2
    msg.extend(['*']*(sq-len(msg)))

    matrix = []
    for i in range(0, sq, int(sqrt(sq))):
        matrix.append(msg[i:i+int(sqrt(sq))])

    # rotate matrix
    matrix = list(zip(*matrix[::-1]))
    print(''.join([''.join(row) for row in matrix]).replace('*', ''))