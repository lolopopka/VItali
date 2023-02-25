line = input().split()
k = 0
for i in range(len(line)):
    k = k + 1
    result = line[k]
    if int(line[i]) < int(result):
        print(result)

#я не знаю как исправить ошибку