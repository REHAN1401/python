def reverseArray(arr, d):
    # n = len(arr)
    # d = d % n
    rotateArray = arr[-d:]+arr[:-d]
    return rotateArray



arr = [1,2,3,4,5]
d = 2
n = len(arr)
x = reverseArray(arr, d)
print(x)