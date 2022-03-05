# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
#
# Pattern: This uses one pass sliding window based solution.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0

        minSize = len(nums)
        runningSum = 0
        subArrayFound = False

        while right < len(nums):

            newelem = nums[right]
            runningSum += newelem

            while runningSum >= target:
                subArrayFound = True
                minSize = min(minSize, right - left + 1)

                leftElem = nums[left]
                runningSum -= leftElem
                left = left + 1

            right = right + 1

        if not subArrayFound:
            return 0

        return minSize