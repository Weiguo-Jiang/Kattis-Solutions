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

angle = int(input())

# try all combinations
for h in range(12):
    for m in range(60):
        # relative to 12 o'clock
        h_angle = 30*h + m/2
        m_angle = 6*m

        # angle from hour hand to minute hand
        d = (m_angle - h_angle) % 360

        if d*10 == angle:
            print("{:02d}:{:02d}".format(h, m))