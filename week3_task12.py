now = int(input())
MaxVar = now
num = 0
while now != 0:
    now = int(input())
    if now > MaxVar:
        MaxVar = now
        num += 1
    if MaxVar != now:
        MaxVar = now
print(num)
