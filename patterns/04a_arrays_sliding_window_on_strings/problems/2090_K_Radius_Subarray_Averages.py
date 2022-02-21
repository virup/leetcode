# 2090. K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/
#

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        l = len(nums)
        slidingWindowLen = 2 * k + 1

        if l < slidingWindowLen:
            return [-1] * l

        if k > l:
            return [-1]

        # We start off with a window of size 'k'
        windowStart = 0
        windowEnd = k
        # This is the first
        currentSum = sum(nums[0:windowEnd])

        # All the arrays which do not have 'slidingWindowLen' items
        # in it have an ave value of -1. So we initialize it first.
        res = [-1] * k

        # Here we run until the windowEnd is less than the len(nums)
        # WindowEnd points to the NEXT item to be added to the list
        # The next item in the window gets added to the running sum as
        # the first step in the loop.
        # For every window of size slidingWindowLen, we take the average and
        # store it. Then we move the windowStart and substract the nums[windowStart]
        # from the running sum
        while windowEnd < len(nums):
            currentSum = currentSum + nums[windowEnd]
            if (windowEnd - windowStart + 1) == slidingWindowLen:
                avg = currentSum // slidingWindowLen
                res.append(avg)
                currentSum = currentSum - nums[windowStart]
                windowStart += 1

            windowEnd += 1

        # Before returning add the -1 for k entries towards the end. These
        # are not windows of size less than slidingWindowLen so we simply put
        # -1 in them.
        return res + [-1] * k
