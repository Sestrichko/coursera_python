N = int(input())
n = 1
k = 0
if N == n:
    print(k)
while N != n:
    n = n * 2
    k = k + 1
    if N == n:
        print(k)
    if N < n:
        print(k)
        break
