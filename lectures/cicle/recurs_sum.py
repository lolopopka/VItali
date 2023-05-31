def get_rec_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+get_rec_sum(arr[1:])
arr = list(map(int, input().split()))
print(get_rec_sum(arr))