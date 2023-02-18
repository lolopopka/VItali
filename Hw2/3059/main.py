n = int(input())
degree = 0
while 2 ** degree < n:
    print(2 ** degree)
    degree += 1