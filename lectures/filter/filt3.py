"""Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
 Реализовать программу с использованием функции filter.
  Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел."""
s = list(map(int, input().split()))
result = filter(lambda x: 10 <= abs(x) <= 99, s)
print(*result)