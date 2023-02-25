line = input().split()
max = -99999
index_of_max = 0
for i in range (len(line)):
    if int(line[i]) > int(max):
        max = (line[i])
        index_of_max = i
    else:
        pass
print(max , index_of_max )





