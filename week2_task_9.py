n = int(input())
if not n == 11 and n % 10 == 1:
    print(f'{n} korova')
elif 2 <= n % 10 <= 4 and (n // 10 > 1 or n // 10 == 0):
    print(f'{n} korovy')
elif n % 5 == 0 or n == 100 or n // 10 >= 1 or 6 <= n <= 9:
    print(f'{n} korov')
