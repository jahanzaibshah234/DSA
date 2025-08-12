class Solution:
    def sumOfDigits(self, n):
        # code here
        sum = 0
        for i in range(n):
            digit = n % 10
            sum += digit
            n = n // 10
        return sum