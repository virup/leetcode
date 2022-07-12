# 616. Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/
#
# We use the same method to merge intervals here. The whole program is
# a bit more complicated
# 1. Find the intervals
# 2. Merge the intervals
# 3. Place the <b> tags at the intervals

from typing import List
import heapq

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        intervals = []
        #######################
        # 1. Find the intervals
        #######################
        for i in range(len(s)):
            for w in words:
                l = len(w)
                if i + l > len(s):
                    continue
                if s[i:i + l] == w:
                    intervals.append([i, i + l - 1])

        mergedIntervals = []
        #######################
        # 2. Merge the intervals
        #######################
        heapq.heapify(intervals)

        while len(intervals) > 1:
            # pop two intervals
            # Time complexity: O(1)
            interval1 = heapq.heappop(intervals)
            interval2 = heapq.heappop(intervals)

            # Compare if the intervals overlap
            if interval1[1] < interval2[0] - 1:
                # Since the intervals do not overlap, add the first
                # one to the results array and push the second one
                # back to the heap to be evaluated with a subsequent
                # interval
                mergedIntervals.append(interval1)

                # Time complexity: nO(logn)
                heapq.heappush(intervals, interval2)
            else:
                # The intervals overlap so create a new interval by
                # merging these two intervals and pushing it back
                # to the heap
                tempInterval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

                # Time complexity: nO(logn)
                heapq.heappush(intervals, tempInterval)

        # add the final interval from the heap to the results array
        if len(intervals) > 0:
            mergedIntervals.append(intervals[0])

        #######################
        # 3. Place the <b> tags at the intervals
        #######################
        earlierEnd = -1
        joinRes = []
        for i in range(len(mergedIntervals)):
            curInterval = mergedIntervals[i]
            start = curInterval[0]
            end = curInterval[1]

            joinRes.append(s[earlierEnd + 1:start])
            joinRes.append("<b>")
            joinRes.append(s[start:end + 1])
            joinRes.append("</b>")

            earlierEnd = end

        joinRes.append(s[earlierEnd + 1:])

        return ''.join(joinRes)


