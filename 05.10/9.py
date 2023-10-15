A="ААААBBBCCF"
print(set(A))
for i in set(A):
    c=A.count(i)
    #print(c)
    print(str(A.count(i))+i,end="")
