line = input().split()
for k in range(len(line)):
    line[k] = int(line[k])
for i in range(1, len(line)):
    if line[i] > line[i - 1]:
        print(line[i], end= ' ')
