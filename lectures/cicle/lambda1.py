def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res
string = list(map(int, input().split()))

f1 = lambda cyphers: cyphers < 99999999999999
f2 = lambda cyphers: cyphers if cyphers < 0 else None
f3 = lambda cyphers: cyphers if cyphers >= 0 else None
f4 = lambda cyphers: cyphers >= 3 and cyphers <= 5


for i in [f1, f2, f3, f4]:
    lst = filter_lst(string, i)
    print(*lst)




