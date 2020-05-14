# 356. Line Reflection.py
# https://leetcode.com/problems/line-reflection/
# This solution has the following steps:
# 1. Find the possible reflection line by summing all the x coordinates and 
#    dividing by the number of UNIQUE points
# 2. For each point in the input list, find its reflected point (reflected on 
#    reflection line found in step 1) and check if the reflected point is
#    present in the input points list.
#
# The runtime is O(n)
# There are two loops, each run in O(n)

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        pointset = set() # To store only the unique points
        
        # Compute the sum of all the x coordinates of all 
        # the UNIQUE points in the given points. We will 
        # use this later to compute the possible reflection
        # line.
        totalXCoordSum = 0 
        for p in points:
            if (p[0], p[1]) not in pointset:
                pointset.add((p[0], p[1]))
                # sum all the x values
                totalXCoordSum += p[0]
            
        # Get the possible reflection line 
        midpointY = totalXCoordSum / len(pointset)
        
        # For every point in the input, check if there
        # is a reflected point present in the pointset
        # If no such point is present, return false
        for p in points:
            x = p[0]
            y = p[1]
            reflectedPoint = (2 * midpointY - x, y)
            if reflectedPoint not in pointset:
                return False
        return True
