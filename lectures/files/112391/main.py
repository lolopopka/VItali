f = open('input.txt', 'r')
output = open('output.txt', 'w')
lines = f.readlines()
print(lines)
sum_of_numbers = 0
quantity = 0
for line in lines:
    quantity += 1
    sum_of_numbers += int(line)
if quantity == 0:
    output.write("0")
else:
    average = sum_of_numbers / quantity
    output.write(str(average))
    output.close()