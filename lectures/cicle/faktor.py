def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)

