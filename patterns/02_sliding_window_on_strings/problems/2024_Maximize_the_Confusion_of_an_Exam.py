# 2024. Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
#

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # initialize the window
        windowStart = 0
        windowEnd = 0

        # Keep a running count of the number of Trues and the Falses
        trueCount = 0
        falseCount = 0

        # This will contain the results
        maxConsecutive = -1

        while windowEnd < len(answerKey):
            # The condition to check for here is whether the count of the smallest
            # answer (T or F) is more than k. If it is, then we do not have the power
            # to swap that many (we can only swap max. k answers). So we try to
            # reduce the window size by incrementing windowStart and removing the left
            # most answer from the counts.
            while min(trueCount, falseCount) > k and windowStart < windowEnd:
                if answerKey[windowStart] == 'T':
                    trueCount -= 1
                else:
                    falseCount -= 1
                windowStart += 1

            # If the count of the min answer is less than k, then this is a valid
            # subarray we can consider as a potential candidate. So we try to see if this
            # is the largest subarray.
            if min(trueCount, falseCount) <= k:
                consecutiveLen = windowEnd - windowStart
                maxConsecutive = max(maxConsecutive, consecutiveLen)

            # At the end, try to increase the subarray by one on the right side
            if answerKey[windowEnd] == 'T':
                trueCount += 1
            else:
                falseCount += 1

            windowEnd += 1

        # We need to check this at the end for the last element in the answerKey array.
        # We cannot avoid this by making 'windowEnd <= len(answerKey)' (less than and equals)
        # since we are reading the answerKey inside the while loop. So it will result in
        # array out of bounds error 
        if min(trueCount, falseCount) <= k:
            consecutiveLen = windowEnd - windowStart
            maxConsecutive = max(maxConsecutive, consecutiveLen)
        return maxConsecutive
