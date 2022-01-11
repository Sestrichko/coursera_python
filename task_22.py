H = int(input('Высота шеста равна: '))
A_up = int(input('Метры подъема равны: '))
B_down = int(input('Метры спуска равны: '))
print(f'Улитка поднимется за {(H + A_up - B_down - 1) // (A_up - B_down)} дней')
