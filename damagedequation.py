a, b, c, d = input().split()
ops = ['*', '+', '-', '//']
flag = False
for op1 in ops:
    for op2 in ops:
        eq = a + ' ' + op1 + ' ' + b + ' ' + '==' + ' ' + c + ' ' + op2 + ' ' + d
        try:
            test = eval(eq)
            if test:
                print(eq.replace('//', '/').replace('==', '='))
                flag = True
        except:
            continue
if not flag:
    print('problems ahead')