# 76. Minimum Window Substring.
# https://leetcode.com/problems/minimum-window-substring/description/
#
# Pattern:
# This problem uses the sliding window pattern.

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        right = 0

        tMap = collections.Counter(t)
        counter = len(tMap)

        minLen = len(s)
        answer = ""

        while right < len(s):

            newch = s[right]
            if newch in tMap:
                tMap[newch] -= 1
                if tMap[newch] == 0:
                    counter -= 1

            while counter == 0 and left <= right:
                leftChar = s[left]
                left = left + 1

                # The left char is not in t, so its a waste char. Resize the window (shrink).
                if leftChar not in tMap:
                    continue

                # If we are here, the chart is in tMap.
                # Case 1: The char is in tMap, but removing it from sliding window does not cause a problem. This is
                # because sliding window already has all instances of tMap including number of characters.
                if tMap[leftChar] < 0:
                    tMap[leftChar] += 1
                    continue

                # If we are here tMap[leftChar] should be equal to zero. If it is greater than zero, we wont come here.

                # Case2: The char is in tMap, but removing its instance from sliding window, makes the sliding window
                # makes the sliding window invalid. This could be a potenantial answer.
                # Note that -2 because we are already doing left = left +1 for convenience.
                newPossibleAnswer = min(minLen, right - left - 2)
                if newPossibleAnswer < minLen:
                    minLen = newPossibleAnswer
                    answer = "".join(s[left - 1:right + 1])

                tMap[leftChar] += 1
                counter = counter + 1

            right = right + 1

        return answer