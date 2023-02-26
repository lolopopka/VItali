from math import inf

nums = input().split()
current_min = inf
for i in range(len(nums)):
    current_num = int(nums[i])
    if current_num % 2 == 1 and current_num < current_min:
        current_min = current_num
if current_min is inf:
    print('0')
else:
    print(current_min)



