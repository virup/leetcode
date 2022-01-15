# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# In this problem, you have to find the next permutation of
# the given sequence.
# The next permutation can be found using the following steps:
#
# 1. Starting the the right end, find the first decreasing element (DE). The index of this positions
#    is called DecreasingElementIndex (DEIndex)
#
# 2. Starting from the DE, find the number on the right of DE which is just
#    larger then DE. This element is called JustLarger (JL) and the position is called JustLargerIndex (JLIndex)
#
# 3. Swap the JL and DE
#
# 4. Reverse all the elements to the right of DEIndex
#
# In this problem, we have to return the result in place so no new array is created

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1. Find the first decreasing element from the right
        DEIndex = -1
        for i in range (len(nums) - 1, -1, -1):
            if nums[i] > nums[i-1]:
                DEIndex = i
                break

        # If there is no such element, then the array is at the last
        # sequence (for ex. [3,2,1]). So simply reverse and return
        if DEIndex == -1:
            nums.reverse()
            return

        # 2. Find the just larger element compared to DE
        JLIndex = len(nums) - 1
        while nums[JLIndex] <= nums[DEIndex]:
            JLIndex -= 1

        if JLIndex == DEIndex:
            # No such element
            JLIndex = len(nums) - 1

        # 3. Swap
        temp = nums[DEIndex]
        nums[DEIndex] = nums[JLIndex]
        nums[DEIndex] = temp

        # 4. Reverse all the elements to the right of DEIndex
        nums[DEIndex + 1:] = nums[DEIndex + 1:][::-1]