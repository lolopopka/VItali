n = input()
first = n.find("h")
second = n.rfind("h")
print(n[0:first] + n[second+1:])
