def compare(array1,array2):
    if len(array1)!=len(array2):
        return False
    else:
        for i in range(0,len(array1)-1):
            if array1[i]!=array2[i]:
                return False
    return True

def compar(array1,array2):
    if array1==array2:
        return True
    else:
        return False

a1 = ["water","book","sky"]
a2 = ["water","book","sky"]
b1 = [True,False]
b2 = [True,False,True]
c1 = [5,3,1]
c2 = [5,3,1]
d1 = [3,2,1]
d2 = [3,2]

print(compare(a1,a2))
print(compare(b1,b2))
print(compare(c1,c2))
print(compare(d1,d2))