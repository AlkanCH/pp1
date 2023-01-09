def f(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[0][j] * arr[i][0]:
                return False
    return True

print(f([[1,2],[3,6]]) )