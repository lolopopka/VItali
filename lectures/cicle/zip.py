str = input()
lst = str.split()
while len(lst) % 3 != 0:
    lst.remove(lst[-1])
k = zip(*[iter(lst)]*3)
for x in k:
    print(*x)


