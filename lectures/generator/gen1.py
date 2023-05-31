"""Подвиг 1. Вводится натуральное число N.
 Необходимо определить функцию-генератор с именем get_sum,
 которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:

- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1+2 = 3
....
- для N-го числа сумма равна 1+2+...+(N-1)+N

Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить."""


def get_sum(N):
    temp_sum = 0
    for i in range(1, N + 1):
        temp_sum += i
        yield temp_sum