# 1852. Distinct Numbers in Each Subarray
# https://leetcode.com/problems/distinct-numbers-in-each-subarray/
#

from collections import defaultdict
from typing import List

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        slidingWindow = defaultdict(int)
        results = []

        # A running counter of the number of distinct elements in
        # the sliding window at any time
        distinctNumberCount = 0
        for i in range(len(nums)):
            if i >= k:
                # Since the sliding window size is fixed, every time
                # we go over k items in the window, we remove the
                # leftmost item from the list
                removeCh = nums[i - k]
                slidingWindow[removeCh] -= 1
                if slidingWindow[removeCh] == 0:
                    del slidingWindow[removeCh]
                    distinctNumberCount -= 1

            addCh = nums[i]
            if addCh not in slidingWindow:
                distinctNumberCount += 1

            slidingWindow[addCh] += 1

            if i >= k - 1:
                results.append(distinctNumberCount)

        return results
