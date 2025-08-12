#User function Template for python3

class Solution:
	def distance(self, x1, y1, x2, y2):
		# Code here
		import math
		point1 = (x1, y1)
		point2 = (x2, y2)
		distance = math.dist(point1, point2)
		roun_num = round(distance)
		return roun_num