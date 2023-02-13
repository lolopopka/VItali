qual = int(input())
counter0 = 0
counter_more_then_0 = 0
counter_lower_then_0 = 0
for i in range(qual):
    nums = int(input())
    if nums > 0:
        counter_more_then_0 += 1
    elif nums < 0:
        counter_lower_then_0 += 1
    else:
        counter0 += 1
print(counter0, counter_more_then_0, counter_lower_then_0)
