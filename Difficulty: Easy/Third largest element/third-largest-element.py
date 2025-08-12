class Solution:
    def thirdLargest(self,arr):
        # code here
        n = len(arr)
        
        if n < 3:
            return -1
        
        arr.sort()
        
        
        for i in range(n -3, -1, -1):
            if i == n -3 or arr[i] != arr[n-1]:
                return arr[i]
        
        return -1