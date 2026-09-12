class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        temp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= temp[1]:
                temp = intervals[i]
            else:
                res+=1
                if temp[1] > intervals[i][1]:
                    temp = intervals[i]
        return res

