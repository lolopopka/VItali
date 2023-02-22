f = open('input.txt', 'r')
outfile = open('output.txt', 'w')
lines = f.readlines()
array_of_even = []
for line in lines:
    current_number = int(line)
    if current_number > 0 and current_number % 2 == 0:
        array_of_even.append(current_number)
if len(array_of_even) == 0:
    result = "0"
else:
   result = str(min(array_of_even)) +" "+ str(max(array_of_even))
outfile.write(result)
