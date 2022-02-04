now = int(input())
MaxVar = now
Max_2 = 0
while now != 0:
    now = int(input())
    if now <= MaxVar:
        Max_2 = now
    if now > MaxVar and now > Max_2:
        MaxVar = now
print(Max_2)
