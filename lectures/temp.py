def find_all(s):
    answers = []
    i = 0
    while i + 2 < len(s):
        if s[i: i + 2] == 'ра':
            answers.append(i)
        i += 1
    if len(answers) == 0:
        return -1
    return answers


input_string = input()
result = find_all(input_string)
if result == -1:
    print(result)
else:
    print(*result)
