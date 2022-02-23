# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
#
# Pattern: This uses one pass sliding window based solution.
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Current window length.
        count = 0

        # Max window length.
        maxCount = 0

        # Iterate the array
        for i in range(0, len(nums)):
            # If we find one, increase the current window length. If the current window length is greater than
            # max window length, update the maxWindow length.
            if nums[i] == 1:
                count = count + 1
                maxCount = max(maxCount, count)
            else:

                # We have seen a number that is not one. Reset the counter.
                count = 0

        # We are updating the max count every time we see 1. So maxCount will definitely point to the max
        # sliding window length that contains all 1s.
        return maxCount

