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

def no_weekends(moves, p):
    d = dict()
    for i in range(1, 101):
        if i % 7 != 6 and i % 7 != 0:
            d[i] = 0
    for m in moves:
        s, e = m
        flag = False
        for i in range(s, e + 1):
            if i % 7 != 6 and i % 7 != 0 and d[i] < p//2:
                d[i] += 1
                flag = True
                break
        if not flag:
            return False
    return True

def work_weekends(moves, p):
    d = dict()
    for i in range(1, 101):
        d[i] = 0
    for m in moves:
        s, e = m
        flag = False
        for i in range(s, e + 1):
            if d[i] < p//2:
                d[i] += 1
                flag = True
                break
        if not flag:
            return False
    return True


n = int(input())
for _ in range(n):
    m, p = map(int, input().split())
    moves = []
    for _ in range(m):
        b, e = map(int, input().split())
        moves.append((b, e))
    moves.sort()
    if no_weekends(moves, p):
        print("fine")
    elif work_weekends(moves, p):
        print("weekend work")
    else:
        print("serious trouble")