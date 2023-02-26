from math import inf

nums = input().split()
current_min = inf
for i in range(len(nums)):
    current_num = int(nums[i])
    if 0 < current_num < current_min:
        current_min = current_num
print(current_min)
