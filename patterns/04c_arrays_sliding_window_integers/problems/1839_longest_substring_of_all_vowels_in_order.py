# 1839. Longest Substring Of All Vowels in Order.
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
#
# Pattern: This uses one pass sliding window based solution.

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        left = 0
        right = 0

        maxLen = 0
        window = set()
        currentWindoIndex = 0

        while right < len(word):

            nc = word[right]

            # Check if the new character is going to make the existing sliding window
            # invalid. If we newly joining character in sliding window is less than the
            # previous character ("a" < "e" < "i" < "o" < "u"), then the sliding window is               # invalid.
            if right > 0 and nc < word[right - 1]:
                window = set()
                left = right

            window.add(nc)

            if len(window) == 5:
                maxLen = max(maxLen, right - left + 1)

            right = right + 1

        return maxLen