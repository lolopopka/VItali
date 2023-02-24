line = input().split()
k = 0
for i in range(len(line)):
    k = k + 1
    result = int(line[k])
    if int(line[i]) < result:
        print(result)

#я не знаю как исправить ошибку