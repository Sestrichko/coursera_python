N = int(input())
n = 1
if N == 0:
    print('NO')
while n <= N:
    n = n * 2
    if n == N or N == 1:
        print('YES')
        break
    if n > N:
        print('NO')
        break
