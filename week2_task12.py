cell1ver = int(input())
cell1hor = int(input())
cell2ver = int(input())
cell2hor = int(input())
if (cell1ver < cell2ver <= 8) and (cell1hor < cell2hor <= 8):
    print('YES')
elif (cell2ver < cell1ver <= 8) and (cell1hor < cell2hor <= 8):
    print('YES')
else:
    print('NO')