"""Подвиг 6. Вводятся данные в формате ключ=значение в одну строчку через пробел.
 Необходимо на их основе создать словарь d,
 затем удалить из этого словаря ключи 'False' и '3',
  если они существуют. Ключами и значениями словаря являются строки.
   Вывести полученный словарь на экран командой:"""

string = input()
sort_string = string.replace('=', ' ')
d = sort_string.split()
dict = {d[i - 1]: d[i] for i in range (1, len(d), 2)}
dict.pop('3')
dict.pop('False')
print(*sorted(dict.items()))





