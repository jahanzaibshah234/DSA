class Solution:
    def removeDuplicates(self, arr):
        # code here 
        new_arr = []
        
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                new_arr.append(arr[i])
        new_arr.append(arr[-1])
                
        return new_arr