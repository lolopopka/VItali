f = open('input.txt', "r")
outfile = open("output.txt", 'w')
lines = f.readlines()
number_of_words = 0
for line in lines:
    number_of_words += len(list(line.split()))
outfile.write(str(number_of_words))