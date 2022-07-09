# 759. Employee Free Time
# https://leetcode.com/problems/employee-free-time/
#


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        allSchedules = []

        # Create a flattened list containing all the busy schedules
        for ss in schedule:
            for s in ss:
                allSchedules.append(s)

        # Sort all the busy schedules based on the start times
        sortedSchedule = sorted(allSchedules, key=lambda x: x.start)

        temp = sortedSchedule[0]
        result = []

        for s in sortedSchedule:
            # check if the schedule overlaps with the previous one
            if temp.end < s.start:
                # Does not overlap. So its a candidate for a free interval
                result.append(Interval(temp.end, s.start))
                temp = s
            else:
                # Does overlap
                # Find the interval which ends later on. Use that for comparing the
                # next schedule
                if temp.end < s.end:
                    temp = s

        return result