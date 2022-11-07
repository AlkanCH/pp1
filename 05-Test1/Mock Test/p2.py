def f(binary_number):
    for i in range(0,len(binary_number),1):
        if binary_number[i]!='0' and binary_number[i]!='1':
            return False
    return True