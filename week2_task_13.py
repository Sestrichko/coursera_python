a = int(input())
b = int(input())
c = int(input())
if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print('impossible')
elif (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
    print('rectangular')
elif c > a and c > b:
    if c**2 < a**2 + b**2:
        print('acute')
    if c**2 > a**2 + b**2:
        print('obtuse')
elif a > b and a > c:
    if a**2 < b**2 + c**2:
        print('acute')
    if a**2 > b**2 + c**2:
        print('obtuse')
elif b > a and b > c:
    if b**2 < a**2 + c**2:
        print('acute')
    if b**2 > a**2 + c**2:
        print('obtuse')
elif a == b == c:
    print('acute')
