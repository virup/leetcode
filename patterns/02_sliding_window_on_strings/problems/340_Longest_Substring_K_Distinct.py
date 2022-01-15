class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        # Set the pointers of the sliding window
        windowStart = 0
        windowEnd = 0

        # Create the window
        slidingWindow = {}

        # Store the results
        maxCount = 0

        # Iterate over the string
        while windowEnd < len(s):

            # Extract the character at windowEnd to check
            ch = s[windowEnd]

            if ch in slidingWindow:
                slidingWindow[ch] += 1
            else:
                slidingWindow[ch] = 1

            # check to satisfy the condition. In this
            # the number of distinct characters should not
            # be more than k
            while len(slidingWindow) > k and windowStart < windowEnd:
                removeCh = s[windowStart]
                slidingWindow[removeCh] -= 1
                if slidingWindow[removeCh] == 0:
                    del slidingWindow[removeCh]
                windowStart += 1

            maxCount = max(maxCount, windowEnd - windowStart + 1)

            # update the windowEnd
            windowEnd += 1

        return maxCount