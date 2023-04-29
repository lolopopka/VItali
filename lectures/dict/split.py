s = "1 - 2 - 3"
s = "".join(s.split())
if s.find('-') > -1:
    a = s.split('-')
    result = 0
    b = list(map(int, a[0].split('+')))
    result += sum(b)
    for i in a[1:]:
        nums = list(map(int, i.split('+')))
        result += -nums[0] + sum(nums[1:])
    print(result)
else:
    a = list(map(int, s.split('+')))
    print(sum(a))




