"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda interval:interval.start)

        if not intervals: return True

        end=intervals[0].end

        for i in range(1, len(intervals)):
            start=intervals[i].start
            if start<end:
                return False
            else:
                end=intervals[i].end

        return True