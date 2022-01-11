A = int(input('Введите рубли:  '))
B = int(input('Введите копейки: '))
N = int(input('Введите количество пирожков: '))
result = (A * 100 + B) * N
print(f'{result // 100} руб {result % 100} коп')