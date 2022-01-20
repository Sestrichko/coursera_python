k = int(input())
m = int(input())
n = int(input())
if k >= n:
    print(m * 2)
elif (2 * n) % k == 0:
    print((2 * n // k) * m)
elif (2 * n) % k != 0:
    print((2 * n // k) * m + m)
