# put your python code here
def is_even(n):
    return not n % 2

n = int(input())

while n != 1:
    if is_even(n):
        print(n)
    n = int(input())
