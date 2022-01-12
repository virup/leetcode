# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        # Set the pointers of the sliding window
        windowStart = 0
        windowEnd = 0

        # Create the window. Stores the number of
        # 0's and 1's
        slidingWindow = {}
        slidingWindow[0] = 0 # This is extraneous and we can remove
        slidingWindow[1] = 0 # We only need to store the number of 0's

        # Store the results
        maxCount = 0

        # Iterate over the string
        while windowEnd < len(A):

            # Extract the character at windowEnd to check
            ch = A[windowEnd]

            slidingWindow[ch] += 1

            # check to satisfy the condition. In this
            # case count of the character "0" should not be
            # already more than K.
            #
            # Note: We are doing "windowStart <= windowEnd", that is,
            # less than and equal to and not just "<".
            while slidingWindow[0] > K and windowStart <= windowEnd:
                removeCh = A[windowStart]
                slidingWindow[removeCh] -= 1
                windowStart += 1

            maxCount = max(maxCount, windowEnd - windowStart + 1)

            # update the windowEnd
            windowEnd += 1

        return maxCount