def dec_to_bin(num):
    result = ""
    while num > 0:
        result =str(num % 2) + result
        num = num // 2
    return result
print(dec_to_bin(10))
print(int("111", 2))