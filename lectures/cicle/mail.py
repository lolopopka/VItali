
"""Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения:
 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом."""


import string
letters = string.ascii_letters
cyphers = '0123456789@_.'
all_sym = letters + cyphers
def is_mail_correct(x):
    if set(x) <= set(all_sym) and '@' in x and '.' in x:
        return True
    else:
        return False






if is_mail_correct(input()):
    print('ДА')
else:
    print("НЕТ")