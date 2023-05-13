def get_biggest_city(*args):
    max_len = -1
    name_biggest_city = ''
    for i in args:
        if len(i) > max_len:
            max_len = len(i)
            name_biggest_city = i
    return name_biggest_city