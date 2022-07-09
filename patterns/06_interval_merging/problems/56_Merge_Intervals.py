# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
#
# Here we use the interval merging technique but instead of
# adding an external interval, we just use the given set of intervals

import heapq
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Create the initial intervals list
        # Time complexity: O(n)
        # Memory complexity: O(n)
        heapq.heapify(intervals)

        results = []

        while len(intervals) > 1:
            # pop two intervals
            # Time complexity: O(1)
            interval1 = heapq.heappop(intervals)
            interval2 = heapq.heappop(intervals)

            # Compare if the intervals overlap
            if interval1[1] < interval2[0]:
                # Since the intervals do not overlap, add the first
                # one to the results array and push the second one
                # back to the heap to be evaluated with a subsequent
                # interval
                results.append(interval1)

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
        results.append(intervals[0])

        return results