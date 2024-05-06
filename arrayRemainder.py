def arrayRem(arr, n):
    x = 1
    for num in arr:
        x = (x * num)%n
    return x

arr = [100, 10, 5 ,25, 35, 10]
n = 11
print("The result is: ",arrayRem(arr, n))