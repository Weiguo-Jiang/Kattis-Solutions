#
# BEGIN-HEADER
#
# Name: Weiguo Jiang
#
# Student-ID: 1670913
#
# By submitting this code, you are agreeing that you have solved in accordance
# with the collaboration policy in CMPUT 303/403.
#
# END-HEADER
#

from math import ceil

while True:
    try:
        inp = input()
    except EOFError:
        break

    n = int(inp)

    # determine interval for iteration
    l = ceil(len(inp)/3)
    ub = 10**l+1
    lb = 10**(l-1)

    # since n is not necessarily a perfect cube,
    # therefore binary search may not converge
    while abs(ub-lb) > 1:
        m =  (lb + ub)//2
        cube = m**3

        if cube == n:
            ub = m
            lb = m
            break
        elif cube > n:
            ub = m
        else:
            lb = m

    # calculate difference from n
    ub_d = abs(ub**3-n)
    lb_d = abs(lb**3-n)

    if ub_d < lb_d:
        print(ub)
    else:
        print(lb)