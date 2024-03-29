"""Подвиг 3. Вводится натуральное число N (N > 8).
Необходимо определить функцию-генератор, которая бы выдавала пароль длиной N символов из случайных букв,
 цифр и некоторых других знаков.
  Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки:
   ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и делать это бесконечно,
 то есть, вызывать ее можно бесконечное число раз.
 Сгенерировать случайный индекс indx в диапазоне [a; b] для символа можно с помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).

Sample Input:

10
Sample Output:

riGp?58WAm
!dX3a5IDnO
dcdbWB2d*C
4?DSDC6Lc1
mxLpQ@2@yM"""

from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

import random

random.seed(1)
"indx = random.randint(a, b)"


def gen_password(N):
    from string import ascii_lowercase, ascii_uppercase
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    password = ''
    for j in range(5):
        for i in range(N):
            index = random.randint(0, len(chars))
            password = password + chars[index]
        yield password
        password = ''


N = int(input())
lst = [i for i in gen_password(N)]
for i in lst:
    print(i)
