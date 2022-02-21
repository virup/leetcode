# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# This pattern uses two pointers (windowStart, and windowEnd) to iterate over
# the given string. They both start from the first position (index 0). At every
# iteration, we first extract the character (ch) at the windowEnd position. We check
# to see if adding this new character (ch) in the window would statisfy the condition
# we are looking for. In this case, we do not want any repeating characters. We
# maintin our window in a set "m". So we we check to see if the set "m" contains the
# new character "ch". If yes, we iteratively remove characters from the windowStart,
# and move the windowStart pointer to the right one at a time until the "ch" is not
# present in the window "m". After this, we add "ch" in "m" as it is not repeated any
# longer. We shift the windowEnd point one position to the right. We compute the
# window size and keep track of the biggest window at every iteration of windowEnd.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Set the pointers of the sliding window
        windowStart = 0
        windowEnd = 0

        # Create the window
        slidingWindow = set()

        # Store the results
        maxCount = 0

        # Iterate over the string
        while windowEnd < len(s):

            # Extract the character at windowEnd to check
            ch = s[windowEnd]

            # check to satisfy the condition. In this
            # case the character "ch" should not be already
            # present in the window
            while ch in slidingWindow and windowStart < windowEnd:
                slidingWindow.remove(s[windowStart])
                windowStart += 1

            # At this point ch is completely removed from the sliding window if it exists.

            # Add the new character to the window
            slidingWindow.add(ch)
            maxCount = max(maxCount, windowEnd - windowStart + 1)

            # update the windowEnd
            windowEnd += 1

        return maxCount