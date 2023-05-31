"""Подвиг 7. Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает False,
 если длина строки меньше 6 символов. Иначе возвращается значение True.

После объявления функции прочитайте (с помощью функции input) список названий городов, записанных в
одну строку через пробел.
Затем, используя генератор списка и созданную функцию, сформируйте список из названий городов длиной не менее шести символов на основе введенного исходного списка.
 Результат отобразите на экране командой:

print(*lst)

где lst - итоговый сформированный список.

Sample Input:

Москва Уфа Пермь Самара Вологда
Sample Output:

Москва Самара Вологда"""

'''result = []
def city(x):
    cities = x.split()
    for i in range(len(cities)):
        if len(cities[i]) >= 6:
             result.append(cities[i])
    return result
print(*city(input()))

cities = x.split()
result = [x for x in cities if len(x) >= 6]'''


def less_six(x):
    if len(x) >= 6:
        return True
    else:
        return False


x = input()
cities = x.split()
result = [x for x in cities if less_six(x)]
print(*result)
