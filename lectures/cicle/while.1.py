def square(x):
    numbers = x.split()
    beginn = int(numbers[0])
    while beginn ** 2 <= int(numbers[1]) ** 2:
        print(beginn ** 2, end=' ')
        beginn += 1


square(input())
