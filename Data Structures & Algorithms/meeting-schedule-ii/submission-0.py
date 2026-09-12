"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda x: (x.start))
        temp = []

        for i in range(len(intervals)):
            if temp and temp[0] <= intervals[i].start:
                heapq.heappop(temp)
            heapq.heappush(temp, intervals[i].end)
        
        return len(temp)

