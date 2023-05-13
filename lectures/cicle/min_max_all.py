
def min_max_all(x):
    v_min = min(x)
    v_max = max(x)
    v_sum = sum(x)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")
min_max_all(list(map(int, input().split())))
