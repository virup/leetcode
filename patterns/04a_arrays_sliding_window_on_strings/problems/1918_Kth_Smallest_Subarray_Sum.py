# 1918. Kth Smallest Subarray Sum
# https://leetcode.com/problems/kth-smallest-subarray-sum/
#

from typing import List
import sys

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        # In this solution, we find the sum of all possible subarrays
        # and then sort the values. Finally return the value at position k-1.
        # This will be the kth smallest subarray sum.
        # We find the sum of the subarray (i, i + size) by taking the
        # sum of the subarray (i, i + size - 1) and 
        #
        # This solution suffers from time limit exceeded.
        allSums = []
        m = {}

        for size in range(len(nums)):
            s = -sys.maxsize
            for i in range(len(nums) - size):
                if s == -sys.maxsize:
                    s = sum(nums[i:i + size + 1])
                else:
                    s = s - nums[i - 1] + nums[i + size]

                allSums.append(s)

        return sorted(allSums)[k - 1]

