array1=[4,36,12,28,9,44,5]
array2=[5,1,36]
result=[]
for i in range(0,len(array1)):
    for j in range(0,len(array2)):
        if array1[i]==array2[j]:
            break
    
        if j == len(array2)-1:
            result.append(array1[i])

print(result)