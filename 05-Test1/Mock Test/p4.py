def f(number, even):
    number=str(number)
    sum=0
    for i in range(0,len(number),1):
        if (int(number[i])%2==0) == even:
            sum+=int(number[i])
   
    return sum