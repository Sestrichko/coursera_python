now = int(input())
num = 0
while now > 0:
    now = int(input())
    num += 1
    if now == 0:
        now = int(input())
        print(num)
