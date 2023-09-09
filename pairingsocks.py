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


from collections import deque

# dq1 is original pile, dq2 auxiliary pile
n = int(input())
dq1 = deque(map(int, input().split()))
dq2 = deque()
cnt = 0

while True:
    # if both empty, then we are done
    if not dq1 and not dq2:
        print(cnt)
        break
    # if neither empty, pair if possible,
    # else move top of original to aux
    elif dq1 and dq2:
        if dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
        else:
            dq2.appendleft(dq1.popleft())
    # if original not empty and aux empty, move top
    # of original to top of aux
    elif dq1:
        dq2.appendleft(dq1.popleft())
    # if original empty and aux not, then it's impossible
    elif dq2:
        print("impossible")
        break

    cnt += 1