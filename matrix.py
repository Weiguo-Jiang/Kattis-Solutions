cnt = 1
while True:
    try:
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        empty = input()

    except EOFError:
        break

    print("Case " + str(cnt) + ":")

    k = 1/(a*d-b*c)

    a_inv, b_inv, c_inv, d_inv = d*k, -b*k, -c*k, a*k
    print(int(a_inv), int(b_inv))
    print(int(c_inv), int(d_inv))

    cnt += 1