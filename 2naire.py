def recur(n, t, prize):
    if n == 0:
        return prize

    # expected value if we answer the next question correctly
    expected = recur(n-1, t, prize*2)

    cutoff = prize/expected

    if t > cutoff:
        return (1+t)/2 * expected
    else:
        quit = prize*(cutoff-t)/(1-t)
        answer = (1+cutoff)/2 * expected * (1-cutoff)/(1-t)
        return quit + answer

while True:
    n, t = map(float, input().split())
    if n == 0 and t == 0:
        break
    print(recur(n, t, 1))