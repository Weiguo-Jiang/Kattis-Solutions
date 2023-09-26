q, n, D = map(int, input().split())
f1 = [int(i) for i in input()]
f2 = [int(i) for i in input()]

d = dict()
def hamming_distance(depth, i):
    if depth < 0:
        return 0
    if i == n and depth != 0:
        return 0
    if i == n and depth == 0:
        return 1

    if (depth, i) in d:
        return d[(depth, i)]

    cnt = 0
    if f1[i] == f2[i]:
        cnt += (hamming_distance(depth, i+1) + (q-1)*hamming_distance(depth-2, i+1))
    else:
        if q == 2:
            cnt += 2*hamming_distance(depth-1, i+1)
        else:
            cnt += (2*hamming_distance(depth-1, i+1) + (q-2)*hamming_distance(depth-2, i+1))
    d[(depth, i)] = cnt
    return cnt

print(hamming_distance(D, 0))