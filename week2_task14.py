A = int(input())
B = int(input())
C = int(input())
if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    print('NO')
elif A % 2 != 0 and B % 2 != 0 and C % 2 != 0:
    print('NO')
elif A % 2 == 0:
    if B % 2 != 0 or C % 2 != 0:
        print('YES')
elif B % 2 == 0:
    if C % 2 != 0 or A % 2 != 0:
        print('YES')
elif C % 2 == 0:
    if B % 2 != 0 or A % 2 != 0:
        print('YES')
else:
    print('NO')
