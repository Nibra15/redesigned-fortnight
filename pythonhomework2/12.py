a= input()
b = a.index(">")
b = a[b+1]
c = a.index(";")
d = a.index("&")
c = a [c+1:d]
print(int(b+c)+1)