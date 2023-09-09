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

# number of testcases
T = int(input())

for i in range(T):
    print("Test " + str(i+1))

    # dimension of the testcase
    R, C = map(int, input().split())

    # mirror
    l = []
    for j in range(R):
        l.append(input()[::-1])
    print("\n".join(l[::-1]))