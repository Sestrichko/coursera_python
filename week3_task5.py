X = float(input())
Y = float(input())
varDay = 1
while X <= Y:
    X = X + 0.1 * X
    varDay = varDay + 1
    if X > Y:
        print(varDay)
    if X == 0:
        break
