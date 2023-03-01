words = {}
f = open('input.txt', 'r')
lines = f.readlines()
for line in lines:
    current_string = line.split()
    for word in current_string:
        if word in words:
            print(words[word], end=' ')
            words[word] += 1
        else:
            print('0', end=' ')
            words[word] = 1
