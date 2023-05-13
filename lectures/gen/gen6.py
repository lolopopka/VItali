cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (j for i in range(10000000) for j in cities)
for i in range(20):
    print(next(gen))
