"""Подвиг 8. Вводятся номера телефонов в формате:

номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N

Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени.
 Обратите внимание, что одному имени может принадлежать несколько разных номеров. Полученный словарь вывести командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки."""

import sys
phones = list(map(str.strip, sys.stdin.readlines()))
from collections import defaultdict
phone_book = defaultdict(list)
for i in phones:
    number, name = i.split()
    phone_book[name].append(number)
print(*sorted(phone_book.items()))







