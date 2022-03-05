# 1004. Max Consecutive Ones III.
# https://leetcode.com/problems/max-consecutive-ones-iii/
#
# Pattern: This uses one pass sliding window based solution.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # Sliding window boundaries.
        left = 0
        right = 0

        numZerosInWindow = 0
        maxLen = 0

        while right < len(nums):
            # Get the newly number added to sliding window.
            num = nums[right]

            # If the new number is a zero, increase the number of zeros in window by 1.
            if num == 0:
                numZerosInWindow += 1

            # Check if the current sliding window is invalid. A sliding window in this problem is invalid, if it has
            # more than one zero. If the sliding window is invalid, move the sliding window to left by 1 and continue
            # doing this until sliding window is valid again.
            while numZerosInWindow > k and left <= right:

                if nums[left] == 0:
                    numZerosInWindow -= 1

                # Continue moving the sliding window to left.
                left = left + 1

            # At this point we have a valid sliding window. Check if the new sliding window length is the largest
            # we have seen so
            maxLen = max(maxLen, right - left + 1)

            # Extend the window to right by 1.
            right = right + 1

        return maxLen




