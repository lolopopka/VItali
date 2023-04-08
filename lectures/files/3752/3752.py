nums = list(map(int, input().split()))
a = set()
for i in nums:
    if i in a:
        print("YES")
    else:
        print('NO')
        a.add(i)
