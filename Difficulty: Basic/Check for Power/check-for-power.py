#User function Template for python3
class Solution:
    def isPowerOfAnother (ob,X,Y):
        # code here 
        if Y == 1:
            return True
         
        if X == 1:
            return Y == 1
            
        power = 1
        
        while power < Y:
            power *= X
            if power == Y:
                return True
        return False