n = int(input())
a = 1
b = 1
F_num = 2
k = 3
if n == k:
    print(F_num)
while n != k:
    a = b
    b = F_num
    F_num = a + b
    k += 1
    if n == k:
        print(F_num)
    if n < k and n != 0:
        print(1)
        break
    if n == 0:
        print(0)
        break
