# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# In this problem we should use the pre-sort the given array first before doing anything else
#
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                return True

        return False
