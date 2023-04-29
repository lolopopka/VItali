def min_of_line(line):
    while line.rfind('--') != -1:
        line = line.replace('--', '-')
        print(line)


min_of_line(input())
