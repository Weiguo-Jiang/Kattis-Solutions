x, op, y, eq, z = input().split()
x = [c for c in x]
y = [c for c in y]
z = [c for c in z]

candidates = []
for a in range(len(x)):
    x_prefix = x[:a]
    x_suffix = x[a:]
    for b in range(len(y)):
        y_prefix = y[:b]
        y_suffix = y[b:]
        for c in range(len(z)):
            z_prefix = z[:c]
            z_suffix = z[c:]

            swap1 = (int(''.join(y_prefix + x_suffix)), int(''.join(x_prefix + y_suffix)), int(''.join(z)))
            swap2 = (int(''.join(z_prefix + x_suffix)), int(''.join(y)), int(''.join(x_prefix + z_suffix)))
            swap3 = (int(''.join(x)), int(''.join(z_prefix + y_suffix)), int(''.join(y_prefix + z_suffix)))
            candidates.append(swap1)
            candidates.append(swap2)
            candidates.append(swap3)


for c in candidates:
    expr = str(c[0]) + ' ' +  op + ' ' +  str(c[1]) + ' ' + '==' + ' ' + str(c[2])
    if eval(expr):
        print(expr.replace('==', '='))
        exit(0)