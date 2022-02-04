A = int(input())
a = 1
b = 1
F_num = 2
k = 3
if A == F_num:
    print(k)
while A != F_num:
    a = b
    b = F_num
    F_num = a + b
    k += 1
    if A == F_num:
        print(k)
    if A != F_num:
        print(-1)
        break
    if A == 1:
        print(1)
        break
    if A == 0:
        print(0)
        break
