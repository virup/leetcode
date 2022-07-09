# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
#
# In this pattern we try to use heap to merge an interval
# with a list of intervals.
# We start off by creating a heap and push all the intervals
# into the heap. (heap is ordered based on the first number).
# Then we push the new interval into the heap too. The idea
# here is that when we pick items from the heap, the start intervals
# will be in an increasing order. We will repeatedly pull the top
# two intervals from the heap, check to see if they overlap, and if
# they do, then create a new interval by merging them and insert the
# new interval in the heap. If the intervals do not merge, then add the
# first one into the result and the second one into the heap.

from typing import List
import heapq

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # create a heap with all the intervals
        heapq.heapify(intervals)

        # also add the newInterval into the heap
        heapq.heappush(intervals, newInterval)

        # The merged list of intervals
        resultIntervals = []

        while len(intervals) > 1:
            # pick the first two intervals from the heap
            interval1 = heapq.heappop(intervals)
            interval2 = heapq.heappop(intervals)

            # Check if the heaps overlap

            # Checking if end of the second interval is lower than the start of the
            # first interval OR the start of the first interval is higher than the
            # end of the second interval
            if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
                # The intervals do not overlap

                # store the first interval in the result and push the
                # second interval in the heap to be evaluated further to see
                # if the second interval merges with any other intervals.
                resultIntervals.append(interval1)
                heapq.heappush(intervals, interval2)
            else:
                # The intervals overlap so merge them.
                tempInterval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

                # Push the merged interval to the heap so that it can be compared
                # with subsequent intervals in the next while loop to see if it merges with
                # any other intervals.
                heapq.heappush(intervals, tempInterval)


        # Check to see if there is any remaining interval in the
        # heap. If yes, add it to the result.
        if len(intervals) > 0:
            resultIntervals.append(intervals[0])

        return resultIntervals
