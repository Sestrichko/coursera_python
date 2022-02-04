now = int(input())
VarSum = now
while now > 0:
    now = int(input())
    VarSum += now
    if now == 0:
        print(VarSum)
