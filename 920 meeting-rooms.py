"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        if len(intervals) <= 1:
            return True
        length = len(intervals)
        test1 = sorted(intervals, key=lambda x: x[0])
        for i in range(length - 1):
            if intervals[i][1] <= intervals[i + 1][0]:
                continue
            else:
                return False
        return True
