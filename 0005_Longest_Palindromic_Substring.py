# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#
# The solution using memoization, which is a form of dynamic programming.
# We first mark all single letter substrings in the string as palindrome.
# We then run another loop to see if any two letter substrings are
# palindrome or not. This information is stored in the 2-D array 'm'.
# From then on, in a loop, we iteratively figure out whether 3, 4, 5
# and so length of substrings are palindrome using the (n-2) length
# palindromes. If substring of size 'n' is a palindrome, and the
# letters around the substring are same, then the substring of size
# n+2 is also a palindrome.

class Solution:
    def __init__(self):
        pass

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        w = len(s)
        h = len(s)

        # Create the 2D array for memoization
        # Each item in this array contains an integer indicating the
        # size of the palindrome starting att he first index and endin at the second index.
        # -1 indicates no palindrome
        m = [[0 for x in range(w)] for y in range(h)]

        highest = 1 # Stores the length of the longest palindrome substring seen till now
        hStart = 0  # Start index of the longest palindromic substring
        hEnd = 0    # End index of the longest palindromic substring

        # Mark all substrings of size 1 as a palindrome
        for i in range(len(s)):
            m[i][i] = 1

        # Evalute all the substrings of size 2 as palindrome or not.
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                m[i][i + 1] = 2
                highest = 2
                hStart = i
                hEnd = i + 1
            else:
                m[i][i + 1] = -1

        # Step is the size of the substrings to evaluate
        for step in range(2, len(s)):
            # I is the start of the substring to evaluate
            for i in range(len(s) - step):
                st = i        # Start index of the substring to evaluate
                e = i + step  # End index of the substring to evaluate
                # If the inner substring is a palindrome and outer letters
                # are the same, mark is as a palindrome
                if m[st + 1][e - 1] != -1 and s[st] == s[e]:
                    l = m[st + 1][e - 1] + 2
                    m[st][e] = l
                    if l > highest:
                        highest = l
                        hStart = st
                        hEnd = e
                else:
                    m[st][e] = -1

        return s[hStart:hEnd + 1]