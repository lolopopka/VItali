line = input()
result = ''
for i in range (len(line)):
    if i % 3 != 0:
        result += line[i]
print(result)

