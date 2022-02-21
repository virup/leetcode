# 30. Substring with Concatenation of All Words.
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/submissions/
#
# Pattern:
# This problem uses the sliding window pattern.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        windowStart = 0
        windowEnd = 0

        charCountMap = {}
        maxLen = 0

        while windowEnd < len(s):

            # Get the new character at the window end. This is the newly added char in sliding window.
            ch = s[windowEnd]

            # Check if this character is present in the current charCountMap.
            if ch in charCountMap:
                charCountMap[ch] += 1
            else:
                # If it is not present
                charCountMap[ch] = 1

            # There should be atleast 2 characters in the count map. This will transalte to atleast 2 unique
            while len(charCountMap) > 2 and windowStart < windowEnd:

                # This means, we can remove the character from the beginning of the sliding window. This is
                # in effort to keep the numberof uniqe characters in the sliding window to atmost 2.
                sc = s[windowStart]
                charCountMap[sc] -= 1

                # Delete the character in the hash map that has no counts. This will make
                # ch in charCountMap easy above  and len(charCountMap) > 2
                if charCountMap[sc] == 0:
                    del charCountMap[sc]

                # Move the window start to left by 1. Continue doing this process until the sliding window has atmost
                # 2 unique characters.
                windowStart += 1

            maxLen = max(maxLen, windowEnd - windowStart + 1)

            # Increase the sliding window length by 1.
            windowEnd += 1

        return maxLen
