user_number = int(input('Введите трехзначное число: '))
print((user_number % 10) + (user_number // 10 % 10) + user_number // 100)