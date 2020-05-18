# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# The solution uses a window over the string
# 1. Keep a list of all the unique characters seens in the window in a set called includedChars
# 2. Check the character at the end of the window (windowEnd). If it is not part of the 
#    includedChars set, then add it to the set and extend the window end.
#    If it is part of the set (which means it is a duplicated character), then move the start
#    of the window by one (windowStart) and remove the character at the begining of the window
#    from the includedChars list.
# 3. Finally, keep a count of the size of the includedChars set. The largest size of that set
#    will be the final answer.
#
# The runtime complexity of this algorighm is O(n), where n in the number of chars in the string s.
# The loop in line 25 runs over all the characters in the the string s once thus making the runtime
# complexity O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        includedChars = set()
        substringLen = 0
        windowStart = 0
        windowEnd = 0
        
        while windowEnd < len(s):
            if s[windowEnd] not in includedChars:
                includedChars.add(s[windowEnd])
                windowEnd +=1 
            else:
                includedChars.remove(s[windowStart])
                windowStart +=1
            substringLen = max(len(includedChars), substringLen)
        return substringLen
