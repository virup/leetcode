# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# The time complexity for this is O(26 )N. Here max(counterMap.values()) is skipped by the help
# of maxF. The idea here is maxF+k >= ans. Unless there is new maxF, the answer is not going to change.
# So keep the maxF variable consistent. Instead of find max of dictioinary values, we can piggy back
# on this variable. This will reduce the time complexity to O(N).

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        windowStart = 0
        windowEnd = 0

        counterMap = {}
        maxLen = 0
        maxF = 0

        while windowEnd < len(s):

            # Get new character that is newly added into sliding window.
            ch = s[windowEnd]
            if ch in counterMap:
                counterMap[ch] += 1
            else:
                counterMap[ch] = 1

            # Update the max freequency if needed. Note that maxF is not the maximum freequency of the character in the entire string. It is just the max freeuency in the sliding window. Note that we are decrementing it as well.
            maxF = max(maxF, counterMap[ch])

            # If the sliding window length - max freequency is greater than K, there is more than 1 character
            # atleast that we cannot replace with character of max freequency to satisfy the question.
            # Keep moving left.
            while (windowEnd - windowStart + 1 - maxF) > k and windowStart < windowEnd:
                # Get the first character in the list and remove it from the dict. This is because
                # we are about to slide left and the the character in the begining of the sliding
                # window should not be in the map.
                sc = s[windowStart]
                counterMap[sc] -= 1

                if counterMap[sc] == 0:
                    del counterMap[sc]

                # Slide left:
                windowStart = windowStart + 1

            maxLen = max(maxLen, windowEnd - windowStart + 1)
            windowEnd = windowEnd + 1
        return maxLen