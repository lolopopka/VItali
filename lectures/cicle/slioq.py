# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()
a = []
for i in s_lst:
    key, value = i.split('=')
    t = tuple((key, value))
    a.append(t)
print(tuple(a))


