now = int(input())
num = 0
if now % 2 == 0 and now != 0:
    num = 1
while now != 0:
    now = int(input())
    if now % 2 == 0 and now != 0:
        num += 1
print(num)
