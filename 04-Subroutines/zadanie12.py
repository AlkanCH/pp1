def sum(N+1):
    if N==0:
        return 1
    else:
        return N+sum(N-1)

print(sum(10))