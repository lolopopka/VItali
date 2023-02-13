counter = 0
numbers = int(input())
for i in range (numbers):
    nums = int(input())
    if nums > 0:
        pass
    elif nums == 0:
        counter += 1
    else:
        break
print (counter)
