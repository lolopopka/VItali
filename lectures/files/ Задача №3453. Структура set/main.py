#https://informatics.msk.ru/mod/statements/view.php?id=25419&chapterid=3453#1
num = int(input())
a = set()
for i in range(num):
    operation = input().strip().split()
    if len(operation) == 2:
        if operation[0] == "ADD":
            a.add(int(operation[1]))
        else:
            if int(operation[1]) in a:
                print('YES')
            else:
                print("NO")
    else:
        print(len(a))
