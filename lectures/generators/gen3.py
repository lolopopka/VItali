import sys

# считывание списка из входного потока
lst_in = input().split()
# здесь продолжайте программу (используйте список lst_in)
result = {i.upper() for i in lst_in if len(i)>2}

"""
result = set()
for i in lst_in:
    if len(i) > 2:
        result.add(i.upper())
"""



print(len(result))