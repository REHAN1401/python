def spliArray(arr, k):
    n = len(arr)
    if k==0 or k<n:
        print("invalid roation value")
        return arr

    x = arr[k:]+arr[:k]
    return x

arr = [1,2,3,4,5,6]
k = 7
ans = spliArray(arr, k)
print(ans)
