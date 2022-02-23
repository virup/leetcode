# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
#
# Pattern: This uses one pass sliding window based solution. This solution does reduced swaps.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Current window length.
        count = 0

        # Max window length.
        maxCount = 0

        # Iterate the array
        for i in range(0, len(nums)):
            # If we find one, increase the current window length. Note that we are not updating max count here
            # to avoid unnecessary comparisions.
            if nums[i] == 1:
                count = count + 1
            else:
                # We have seen a number that is not one. Reset the counter and update max count.
                maxCount = max(maxCount, count)
                count = 0

        # We are not updating the max count every time. We are updating only if we see a non "1". So if the array ends with series of 1s, the maxcount will not have it. So return max of maxcount and count
        return max(maxCount, count)
