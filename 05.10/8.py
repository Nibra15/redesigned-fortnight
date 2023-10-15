example = "123456"
k = 9
result=[]
for i in range(len(example)):
    for j in range (i+1,len(example)):
        if int(example[i])+int(example[j])== k:
            result.append((example[i],example[j]))
print(result)
