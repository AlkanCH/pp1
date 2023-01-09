array = [4,3,7,1,3]

def sum(array):
    sum=0
    for element in array:
        sum+=element
    return sum

def array2str(array):
    string=""
    return (string.join(array))

print(sum(array))
print(array2str(array))