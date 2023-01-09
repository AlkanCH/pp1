array = [1, 2, 3, 4, 5, 6, 7]

oddcount=0
evencount=0

for num in array:
    if num%2==0:
        evencount+=1

    else:
        oddcount+=1

print("Odd numbers: ", oddcount)
print("Even numbers: ", evencount)
