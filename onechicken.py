N, M = list(map(int, input().split()))
if N <= M:
    leftover = M-N
    if leftover == 0 or leftover == 1:
        print("Dr. Chaz will have " + str(leftover) + " piece of chicken left over!")
    else:
        print("Dr. Chaz will have " + str(leftover) + " pieces of chicken left over!")
else:
    more = N-M
    if more == 0 or more == 1:
        print("Dr. Chaz needs " + str(more) + " more piece of chicken!")
    else:
        print("Dr. Chaz needs " + str(more) + " more pieces of chicken!")