
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        nth = a1
        d = a2 - a1
        
        ap = nth + (n - 1) * d
        return ap
        
