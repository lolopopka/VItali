# put your python code here
n = input()
k = iter(n)
for i in range(0, len(n)):
    print(next(k), end=' ')