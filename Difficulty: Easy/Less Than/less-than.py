def lessThan(arr, k):
    #code here
    ans = []
    for i in range(len(arr)):
        if arr[i] < k:
            ans.append(arr[i])
    return ans
