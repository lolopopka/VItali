line = input().split()
counter = 0
for i in range(len(line)):
    if int(line[i]) > 0:
        counter +=1
    else:
        pass
print(counter)

