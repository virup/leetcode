# 1493. Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
#
# Pattern: This uses one pass sliding window based solution.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # Sliding window boundaries.
        left = 0
        right = 0

        # Max length of sliding window.
        maxLen = 0

        # Number of zeros in window.
        numZerosInWindow = 0

        k = 1

        while right < len(nums):

            elem = nums[right]

            if elem == 0:
                numZerosInWindow += 1

            # Check if the sliding window is invalid. In this problem, the window is invalid if it has more than
            # one zero.
            while numZerosInWindow > k and left <= right:
                leftElem = nums[left]

                if leftElem == 0:
                    numZerosInWindow -= 1

                left += 1

            # At this point, we have a valid sliding window.
            maxLen = max(maxLen, right - left + 1)

            # Move right to increase the size of the sliding window.
            right = right + 1

        # We dont want the element that can deleted. Hence -1.
        return max(maxLen - 1, 0)