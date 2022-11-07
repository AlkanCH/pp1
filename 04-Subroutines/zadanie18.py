def sumdigit(digits):
    sum=0
    for i in range(0,len(digits),1):
        sum+=int(digits[i])
    return sum

print(sumdigit("7182"))