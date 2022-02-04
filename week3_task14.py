now = int(input())
MaxVar = now
num = 1
while now != 0:
    now = int(input())
    if now == MaxVar:
        MaxVar = now
        num += 1
    if now > MaxVar:
        MaxVar = now
print(num)
