#https://informatics.msk.ru/mod/statements/view.php?id=249&chapterid=3060#1
num = int(input())
k = 1
while k != num:
    k *= 2
    if  k > num:
        print('NO')
        break
else:
    print('YES')