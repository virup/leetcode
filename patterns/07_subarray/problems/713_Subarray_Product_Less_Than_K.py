# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/
#
# We have to find the number of contiguous subarrays where the
# product of all the elements in the subarray is strictly less
# than k. We keep a running prefix product variable. Then we convert
# this problem to a sliding window problem.
#
# Runtime complexity: O(n)
# Memory complexity: O(1)

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        prefixProduct = 1
        noOfSubarrays = 0
        windowStart = 0

        for windowEnd in range(len(nums)):
            prefixProduct *= nums[windowEnd]
            while prefixProduct >= k and windowStart <= windowEnd:
                prefixProduct /= nums[windowStart]
                windowStart += 1
            noOfSubarrays += windowEnd - windowStart + 1
        return noOfSubarrays