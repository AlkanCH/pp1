def f(a1,a2):
    sum1=0
    sum2=0

    for i in range(0,len(a1)):
        if str(a1[i]) in ("J","K","Q","A","T"):
            sum1+=10
        else:
            sum1+=int(a1[i])
    
    for i in range(0,len(a2)):
        if str(a2[i]) in ("J","K","Q","A","T"):
            sum2+=10
        else:
            sum2+=int(a2[i])

    if sum1>sum2:
        return True
    else:
        return False

print(f("AJ972","AQT72"))
print(f("9532","K8"))
print(f("987","AT4"))