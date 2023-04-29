input_string = input()
input_string = input_string.replace('=', ' ')
d = input_string.split()
dict = {d[i - 1]: d[i] for i in range(1 , len(d), 2)}
print(dict)
if  'house' in  dict and 'True' in  dict and '5' in  dict:
    print('ДА')
else:
    print('НЕТ')