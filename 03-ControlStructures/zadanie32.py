for i in range(1,8,1):
    for j in range(0,7,1):
        if i+j*7<10:
            print(f" {i+j*7}",end=" ")
        else:
            print(f"{i+j*7}",end=" ")
    print()