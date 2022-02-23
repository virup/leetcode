# 485. Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/
# In this problem we should use the sliding window.
#
# Pattern:
#
# 1. Initialize the sliding window boundaries (left and right).
#
# 2. Extend the sliding window one by right ie add a new character or number ot he sliding window.
#
# 3. Check if the sliding window is valid. Every problem has definition of valid sliding window.
#    In this problem, the window should have atmost one zero and remaining should be 1s.
#
# 4. If the sliding window is invalid, move the window to left by 1.
#
# 5. Continue 3 and 4 until we are left with a new sliding window.
#
# 6. No we are left with a new sliding window. Compute the lenght of the new valid sliding window.
#    If its the greatest we have seen so far, update the current length of sliding window as maximum
#    sliding window.
#
# 7. Repeat 1 - 6 until we are done with all the numbers. After this we can return the max length.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

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
            while numZerosInWindow > 1 and left < right:

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