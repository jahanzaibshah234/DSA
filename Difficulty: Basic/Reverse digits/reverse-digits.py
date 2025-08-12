#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		s = str(n)
		
		reversed_string = s[::-1]
		
		reversed_number = int(reversed_string)
		
		return reversed_number