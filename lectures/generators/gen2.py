a = [1, 2, 3, 4]
for i in a:
    print(i)
for i in range(len(a)):
    print(a[i])
for i in enumerate(a):
    print(i)
for i, g in enumerate(a, start= 100):
    print(i,g)