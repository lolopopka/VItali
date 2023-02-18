def dec_to_any(num, base):
    result = ""
    while num > 0:
        result =str(num % base) + result
        num = num // base
    return result
num = int(input())
print(dec_to_any(num, 2)[::-1])