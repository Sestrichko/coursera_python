now = int(input())
num = 0
VarSum = now
while now != 0:
    now = int(input())
    num += 1
    VarSum += now
    if now == 0:
        print(VarSum / num)
