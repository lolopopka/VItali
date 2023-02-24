with open(r"input.txt", "r", encoding='utf-8') as infile:
    sum_of_numbers = 0
    quantity = 0
    for i in infile:
        sum_of_numbers += int(i)
        quantity += 1

with open(r"output.txt", "w", encoding='utf-8') as outfile:
    outfile.write(str(sum_of_numbers / quantity))