#User function Template for python3
class Solution:
    
    # Function to search for a character in the string
    def searchCharacter(self, s, ch):
        # code here
        for i in s:
            if ch == i:
                return s.index(ch)
        return -1