n = int(input())
y = int(input())
days = 0
while n < y:
    n += (n*0.1)
    days += 1
print(days + 1)
