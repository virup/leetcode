# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#

from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # Each word is of the same length
        lenOfWords = len(words[0])

        # Find the total length of chars when all words are included
        totalWordLen = len(words) * lenOfWords

        windowStart = 0
        windowEnd = 0
        resultIndexes = []


        # Note the <=. The "equals" need to be there otherwise the
        # last character is not considered. If you want to remove the
        # "equals" here, then the check of contains_all() should also
        # he present after this while loop
        while windowEnd <= len(s):
            # If the window is of length greater than the size
            # required to contain all the words, we check to see
            # if the window contains all words. If yes, we append
            # the starting index in the resultIndexes array.
            # After that we shift the window start by one to the right
            while windowEnd - windowStart >= totalWordLen:
                if contains_all(windowStart, windowEnd, s, words):
                    resultIndexes.append(windowStart)
                windowStart += 1

            # We increase the sliding window one char at a time.
            # We cannot increase it by a word length at a time otherwise
            # we will miss words
            windowEnd += 1

        return resultIndexes


def contains_all(windowStart, windowEnd, s, words):
    # In this function we check to see if all the words
    # are contained in the window s(windowStart, windowEnd)
    l = len(words[0])

    m = defaultdict(int)

    # we create a hash of all the word of length l
    # and store it in the variable m.
    for i in range(windowStart, windowEnd, l):
        w = s[i:i + l]
        m[w] += 1

    # For all possible words, we check if m
    # contains the word
    for w in words:
        if w not in m:
            return False
        m[w] -= 1
        if m[w] == 0:
            del m[w]
    return True
