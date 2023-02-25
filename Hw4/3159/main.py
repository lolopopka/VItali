line = input().split()
result_positive_numbers = []
for positive_numbers in range(len(line)):
    if int(line[positive_numbers]) > 0:
        result_positive_numbers += (line[positive_numbers])
    else:
        pass
print(min(result_positive_numbers)) #я забыл как расписывать это без min



