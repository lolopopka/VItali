#https://informatics.msk.ru/mod/statements/view.php?id=25861&chapterid=3762#1
"""
Задача №3762. Самое частое слово
Дан текст (строк может быть много). Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Входные данные
Вводится текст.

Выходные данные
Выведите ответ на задачу.

"""
import collections
array_of_words = input().split()
dict_of_words = {}
for word in array_of_words:
    if word in dict_of_words:
        dict_of_words[word] += 1
    else:
        dict_of_words[word] = 1
max_freq = max(dict_of_words.values())
current_max = 0
result = []
for key, value in dict_of_words.items():
    if value == max_freq:
        result.append(key)
print(min(result))