price = int(input())
sell = input()
if price >= 10000:
    print("Поедем отдыхать в следующем месяце")
elif price < 0:
    print("Ошибка")
elif 0 <= price < 5000:
    print("Покупаем билеты!")
elif 10000 > price >= 5000 and sell == 'да':
    print("Покупаем билеты!")
elif 10000 > price >= 5000 and sell == "нет":
    print("Поедем отдыхать в следующем месяце")

