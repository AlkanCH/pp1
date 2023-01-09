def f(T):

    r=len(T)
    res = []

    for i in range(0,len(T[0])):
        sum=0
        for j in range(0,r):
            sum+=T[j][i]
        res.append(sum)

    print(res)
        
f([[3,6,2,7], [9,5,4,0], [2,8,0,9]])