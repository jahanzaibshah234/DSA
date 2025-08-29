class Solution:
    def isPalindrome(self, s):
        # code here
        for i in s:
            if s == s[::-1]:
                return True
        return False
