num1st = int(input())
num1str = int(input())
num2st = int(input())
num2str = int(input())
if (num2st == (num1st + 1)) and (num2str == (num1str + 1)):
    print('YES')
elif (num2st == (num1st - 1)) and (num2str == (num1str - 1)):
    print('YES')
elif (num2st == (num1st - 1)) and (num2str == (num1str + 1)):
    print('YES')
elif (num2st == (num1st + 1)) and (num2str == (num1str - 1)):
    print('YES')
else:
    print('NO')
