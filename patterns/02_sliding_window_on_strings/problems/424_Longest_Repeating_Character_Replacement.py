# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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

            # check to satisfy the condition.
            while allMoreThanK(slidingWindow, k) and windowStart < windowEnd:
                removeCh = s[windowStart]
                slidingWindow[removeCh] -= 1
                windowStart += 1

            maxCount = max(maxCount, windowEnd - windowStart + 1)

            # update the windowEnd
            windowEnd += 1

        return maxCount

# Returns false if the sum of count of all but one
# character is less than equal to k. In that case,
# we can replace all those characters with the original
# character and get an array of all original characters.
#
# If no such sum exists, then we cannot replace all
# characters with only k. So this is not a valid sub array.
def allMoreThanK(m, k):
    # We consider the fixed character to be the "key"
    for key in m:
        count = 0
        for key2 in m:
            if key == key2:
                continue
            # we sum all the chars which are not "key"
            count += m[key2]
        if count <= k:
            return False
    return True