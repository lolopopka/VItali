n = input()
a = n[:n.find("h")]
c = n[n.find("h") : n.rfind("h")+ 1]
b = n[n.find("h")+ 1:]
print(c[:: -1])

result = a + c[:: -1] + b
print(result)



