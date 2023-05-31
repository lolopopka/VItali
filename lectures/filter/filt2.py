"""Подвиг 2. Вводится список предметов в виде списка:

название_1: вес_1
...
название_N: вес_N

С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж,
 элементами которого также являются кортежи:

(('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))

А, затем, отфильтровать (исключить) все предметы с весом менее 500,
 используя функцию filter.
  Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

зонт=1000
палатка=10000
спички=22
котелок=543
Sample Output:

зонт палатка котелок"""