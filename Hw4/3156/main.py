#https://informatics.msk.ru/mod/statements/view.php?id=2741&chapterid=3156#1
n = input()
c = n.split()
k = []
for i in range(1, len(c)):
    if int(c[i - 1]) > 0 and int(c[i]) > 0:
        k.append([c[i - 1]] + [c[i]])
    if int(c[i - 1]) < 0 and int(c[i]) < 0:
        k.append([c[i - 1]] + [c[i]])
if k == []:
    print()
else:
    print(*k[0])
